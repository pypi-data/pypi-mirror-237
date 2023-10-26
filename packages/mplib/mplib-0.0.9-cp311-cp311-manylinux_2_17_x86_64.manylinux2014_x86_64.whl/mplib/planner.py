from typing import Sequence, Tuple, Union

import os
import numpy as np
from transforms3d.quaternions import quat2mat
import toppra as ta
import toppra.constraint as constraint
import toppra.algorithm as algo

from .pymp import *


class Planner:
    """Motion planner."""

    # TODO(jigu): default joint vel and acc limits
    # TODO(jigu): how does user link names and joint names are exactly used?

    def __init__(
        self,
        urdf: str,
        user_link_names: Sequence[str],
        user_joint_names: Sequence[str],
        move_group: str,
        joint_vel_limits: Union[Sequence[float], np.ndarray],
        joint_acc_limits: Union[Sequence[float], np.ndarray],
        srdf: str = "",
        package_keyword_replacement: str = ""
    ):
        r"""Motion planner for robots.

        Args:
            urdf: Unified Robot Description Format file.
            user_link_names: names of links, the order
            user_joint_names: names of the joints to plan
            move_group: target link to move, usually the end-effector.
            joint_vel_limits: maximum joint velocities for time parameterization,
                which should have the same length as
            joint_acc_limits: maximum joint accelerations for time parameterization,
                which should have the same length as
            srdf: Semantic Robot Description Format file.
        References:
            http://docs.ros.org/en/kinetic/api/moveit_tutorials/html/doc/urdf_srdf/urdf_srdf_tutorial.html

        """
        self.urdf = urdf
        if srdf == "" and os.path.exists(urdf.replace(".urdf", ".srdf")):
            srdf = urdf.replace(".urdf", ".srdf")
            print("No SRDF file provided. Try to load %s." % srdf)
            
        self.srdf = srdf
        self.user_link_names = user_link_names
        self.user_joint_names = user_joint_names

        self.joint_name_2_idx = {}
        for i, joint in enumerate(self.user_joint_names):
            self.joint_name_2_idx[joint] = i
        self.link_name_2_idx = {}
        for i, link in enumerate(self.user_link_names):
            self.link_name_2_idx[link] = i

        # replace package:// keyword if exists
        urdf = self.replace_package_keyword(package_keyword_replacement)

        self.robot = articulation.ArticulatedModel(
            urdf,
            srdf,
            [0, 0, -9.81],
            self.user_joint_names,
            self.user_link_names,
            verbose=False,
            convex=True,
        )
        self.pinocchio_model = self.robot.get_pinocchio_model()

        self.planning_world = planning_world.PlanningWorld(
            [self.robot], ["robot"], [], []
        )

        if srdf == "":
            self.generate_collision_pair()
            self.robot.update_SRDF(self.srdf)

        assert(move_group in self.user_link_names)
        self.move_group = move_group
        self.robot.set_move_group(self.move_group)
        self.move_group_joint_indices = (
            self.robot.get_move_group_joint_indices()
        )

        self.joint_types = self.pinocchio_model.get_joint_types()
        self.joint_limits = np.concatenate(
            self.pinocchio_model.get_joint_limits()
        )
        self.planner = ompl.OMPLPlanner(world=self.planning_world)
        self.joint_vel_limits = joint_vel_limits
        self.joint_acc_limits = joint_acc_limits
        self.move_group_link_id = self.link_name_2_idx[self.move_group]
        assert len(self.joint_vel_limits) == len(
            self.move_group_joint_indices
        ), len(self.move_group_joint_indices)
        assert len(self.joint_acc_limits) == len(self.move_group_joint_indices)

    def replace_package_keyword(self, package_keyword_replacement):
        rtn_urdf = self.urdf
        with open(self.urdf, "r") as in_f:
            content = in_f.read()
            if "package://" in content:
                rtn_urdf = self.urdf.replace(".urdf", "_package_keyword_replaced.urdf")
                content = content.replace("package://", package_keyword_replacement)
                if not os.path.exists(rtn_urdf):
                    with open(rtn_urdf, "w") as out_f:
                        out_f.write(content)
        return rtn_urdf

    def generate_collision_pair(self, sample_time = 1000000, echo_freq = 100000):
        print("Since no SRDF file is provided. We will first detect link pairs that will always collide. This may take several minutes.")
        n_link = len(self.user_link_names)
        cnt = np.zeros((n_link, n_link), dtype=np.int32)
        for i in range(sample_time):
            qpos = self.pinocchio_model.get_random_configuration()
            self.robot.set_qpos(qpos, True)
            collisions = self.planning_world.collide_full()
            for collision in collisions:
                u = self.link_name_2_idx[collision.link_name1]
                v = self.link_name_2_idx[collision.link_name2]
                cnt[u][v] += 1
            if i % echo_freq == 0:
                print("Finish %.1f%%!" % (i * 100 / sample_time))
        
        import xml.etree.ElementTree as ET
        from xml.dom import minidom

        root = ET.Element('robot')
        robot_name = self.urdf.split('/')[-1].split('.')[0]
        root.set('name', robot_name)
        self.srdf = self.urdf.replace(".urdf", ".srdf")

        for i in range(n_link):
            for j in range(n_link):
                if cnt[i][j] == sample_time:
                    link1 = self.user_link_names[i]
                    link2 = self.user_link_names[j]
                    print("Ignore collision pair: (%s, %s), reason:  always collide" % (link1, link2))
                    collision = ET.SubElement(root, 'disable_collisions')
                    collision.set('link1', link1)
                    collision.set('link2', link2)
                    collision.set('reason', 'Default')
        srdffile = open(self.srdf, "w")
        srdffile.write(minidom.parseString(ET.tostring(root)).toprettyxml(indent="    "))
        srdffile.close()
        print("Saving the SRDF file to %s" % self.srdf)

    def distance_6D(self, p1, q1, p2, q2):
        return np.linalg.norm(p1 - p2) + min(
            np.linalg.norm(q1 - q2), np.linalg.norm(q1 + q2)
        )

    def check_joint_limit(self, q):
        n = len(q)
        flag = True
        for i in range(n):
            if self.joint_types[i].startswith("JointModelR"):
                if np.abs(q[i] - self.joint_limits[i][0]) < 1e-3:
                    continue
                q[i] -= (
                    2
                    * np.pi
                    * np.floor((q[i] - self.joint_limits[i][0]) / (2 * np.pi))
                )
                if q[i] > self.joint_limits[i][1] + 1e-3:
                    flag = False
            else:
                if (
                    q[i] < self.joint_limits[i][0] - 1e-3
                    or q[i] > self.joint_limits[i][1] + 1e-3
                ):
                    flag = False
        return flag

    def check_for_collision(self, collision_function, articulation: articulation.ArticulatedModel=None, qpos: np.ndarray=None) -> list:
        # handle no user input
        if articulation is None:
            articulation = self.robot
        if qpos is None:
            qpos = articulation.get_qpos()
        # if the user does not specify the end-effector joints, append them to the qpos
        if len(qpos) == len(self.move_group_joint_indices):
            tmp = articulation.get_qpos()
            tmp[:len(qpos)] = qpos
            qpos = tmp

        # first save the current qpos
        old_qpos = articulation.get_qpos()
        # set robot to new qpos
        articulation.set_qpos(qpos, True)
        # find the index of the articulation inside the array
        idx = self.planning_world.get_articulations().index(articulation)
        # check for self-collision
        collisions = collision_function(idx)
        # reset qpos
        articulation.set_qpos(old_qpos, True)
        return collisions

    def check_for_self_collision(self, articulation: articulation.ArticulatedModel=None, qpos: np.ndarray=None) -> list:
        """Check if the robot is in self-collision.

        Args:
            articulation: robot model. if none will be self.robot
            qpos: robot configuration. if none will be the current pose

        Returns:
            A list of collisions.
        """
        return self.check_for_collision(self.planning_world.self_collide, articulation, qpos)

    def check_for_env_collision(self, articulation: articulation.ArticulatedModel=None, qpos: np.ndarray=None):
        """Check if the robot is in collision with the environment

        Args:
            articulation: robot model. if none will be self.robot
            qpos: robot configuration. if none will be the current pose

        Returns:
            A list of collisions.
        """
        return self.check_for_collision(self.planning_world.collide_with_others, articulation, qpos)


    def IK(self, goal_pose, start_qpos, mask = [], n_init_qpos=20, threshold=1e-3):
        index = self.link_name_2_idx[self.move_group]
        min_dis = 1e9
        idx = self.move_group_joint_indices
        qpos0 = np.copy(start_qpos)
        results = []
        self.robot.set_qpos(start_qpos, True)
        for i in range(n_init_qpos):
            ik_results = self.pinocchio_model.compute_IK_CLIK(
                index, goal_pose, start_qpos, mask
            )
            flag = self.check_joint_limit(ik_results[0]) # will clip qpos

            # check collision
            self.planning_world.set_qpos_all(ik_results[0][idx])
            if (len(self.planning_world.collide_full()) != 0):
                flag = False

            if flag:
                self.pinocchio_model.compute_forward_kinematics(ik_results[0])
                new_pose = self.pinocchio_model.get_link_pose(index)
                tmp_dis = self.distance_6D(
                    goal_pose[:3], goal_pose[3:], new_pose[:3], new_pose[3:]
                )
                if tmp_dis < min_dis:
                    min_dis = tmp_dis
                if tmp_dis < threshold:
                    result = ik_results[0] 
                    unique = True
                    for j in range(len(results)):
                        if np.linalg.norm(results[j][idx] - result[idx]) < 0.1:
                            unique = False
                    if unique:
                        results.append(result)
            start_qpos = self.pinocchio_model.get_random_configuration()
            mask_len = len(mask)
            if mask_len > 0:
                for j in range(mask_len):
                    if mask[j]:
                        start_qpos[j] = qpos0[j]
        if len(results) != 0:
            status = "Success"
        elif min_dis != 1e9:
            status = (
                "IK Failed! Distance %lf is greater than threshold %lf."
                % (min_dis, threshold)
            )
        else:
            status = "IK Failed! Cannot find valid solution."
        return status, results

    def TOPP(self, path, step=0.1, verbose=False):
        N_samples = path.shape[0]
        dof = path.shape[1]
        assert dof == len(self.joint_vel_limits)
        assert dof == len(self.joint_acc_limits)
        ss = np.linspace(0, 1, N_samples)
        path = ta.SplineInterpolator(ss, path)
        pc_vel = constraint.JointVelocityConstraint(self.joint_vel_limits)
        pc_acc = constraint.JointAccelerationConstraint(self.joint_acc_limits)
        instance = algo.TOPPRA(
            [pc_vel, pc_acc], path, parametrizer="ParametrizeConstAccel"
        )
        jnt_traj = instance.compute_trajectory()
        ts_sample = np.linspace(
            0, jnt_traj.duration, int(jnt_traj.duration / step)
        )
        qs_sample = jnt_traj(ts_sample)
        qds_sample = jnt_traj(ts_sample, 1)
        qdds_sample = jnt_traj(ts_sample, 2)
        return ts_sample, qs_sample, qds_sample, qdds_sample, jnt_traj.duration

    def update_point_cloud(self, pc, resolution=1e-3):
        self.planning_world.update_point_cloud(pc, resolution)

    def update_attached_tool(self, fcl_collision_geometry, pose, link_id=-1):
        if link_id == -1:
            link_id = self.move_group_link_id
        self.planning_world.update_attached_tool(fcl_collision_geometry, link_id, pose)

    def update_attached_sphere(self, radius, pose, link_id=-1):
        if link_id == -1:
            link_id = self.move_group_link_id
        self.planning_world.update_attached_sphere(radius, link_id, pose)

    def update_attached_box(self, size, pose, link_id=-1):
        if link_id == -1:
            link_id = self.move_group_link_id
        self.planning_world.update_attached_box(size, link_id, pose)
    
    def update_attached_mesh(self, mesh_path, pose, link_id=-1):
        if link_id == -1:
            link_id = self.move_group_link_id
        self.planning_world.update_attached_mesh(mesh_path, link_id, pose)

    def plan(
        self,
        goal_pose,
        current_qpos,
        mask = [],
        time_step=0.1,
        rrt_range=0.1,
        planning_time=1,
        fix_joint_limits=True,
        use_point_cloud=False,
        use_attach=False,
        verbose=False,
    ):
        self.planning_world.set_use_point_cloud(use_point_cloud)
        self.planning_world.set_use_attach(use_attach)
        n = current_qpos.shape[0]
        if fix_joint_limits:
            for i in range(n):
                if current_qpos[i] < self.joint_limits[i][0]:
                    current_qpos[i] = self.joint_limits[i][0] + 1e-3
                if current_qpos[i] > self.joint_limits[i][1]:
                    current_qpos[i] = self.joint_limits[i][1] - 1e-3


        self.robot.set_qpos(current_qpos, True)
        collisions = self.planning_world.collide_full()
        if len(collisions) != 0:
            print("Invalid start state!")
            for collision in collisions:
                print("%s and %s collide!" % (collision.link_name1, collision.link_name2))

        idx = self.move_group_joint_indices
        ik_status, goal_qpos = self.IK(goal_pose, current_qpos, mask)
        if ik_status != "Success":
            return {"status": ik_status}

        if verbose:
            print("IK results:")
            for i in range(len(goal_qpos)):
               print(goal_qpos[i])

        goal_qpos_ = []
        for i in range(len(goal_qpos)):
            goal_qpos_.append(goal_qpos[i][idx])
        self.robot.set_qpos(current_qpos, True)
        
        status, path = self.planner.plan(
            current_qpos[idx],
            goal_qpos_, 
            range=rrt_range,
            verbose=verbose,
            time=planning_time,
        )

        if status == "Exact solution":
            if verbose:
                ta.setup_logging("INFO")
            else:
                ta.setup_logging("WARNING")

            times, pos, vel, acc, duration = self.TOPP(path, time_step)
            return {
                "status": "Success",
                "time": times,
                "position": pos,
                "velocity": vel,
                "acceleration": acc,
                "duration": duration,
            }
        else:
            return {"status": "RRT Failed. %s" % status}

    def plan_screw(
        self,
        target_pose,
        qpos,
        qpos_step=0.1,
        time_step=0.1,
        use_point_cloud=False,
        use_attach=False,
        verbose=False,
    ):
        self.planning_world.set_use_point_cloud(use_point_cloud)
        self.planning_world.set_use_attach(use_attach)
        qpos = np.copy(qpos)
        self.robot.set_qpos(qpos, True)

        def pose7D2mat(pose):
            mat = np.eye(4)
            mat[0:3, 3] = pose[:3]
            mat[0:3, 0:3] = quat2mat(pose[3:])
            return mat

        def skew(vec):
            return np.array(
                [
                    [0, -vec[2], vec[1]],
                    [vec[2], 0, -vec[0]],
                    [-vec[1], vec[0], 0],
                ]
            )

        def pose2exp_coordinate(pose: np.ndarray) -> Tuple[np.ndarray, float]:
            def rot2so3(rotation: np.ndarray):
                assert rotation.shape == (3, 3)
                if np.isclose(rotation.trace(), 3):
                    return np.zeros(3), 1
                if np.isclose(rotation.trace(), -1):
                    return np.zeros(3), -1e6
                theta = np.arccos((rotation.trace() - 1) / 2)
                omega = (
                    1
                    / 2
                    / np.sin(theta)
                    * np.array(
                        [
                            rotation[2, 1] - rotation[1, 2],
                            rotation[0, 2] - rotation[2, 0],
                            rotation[1, 0] - rotation[0, 1],
                        ]
                    ).T
                )
                return omega, theta

            omega, theta = rot2so3(pose[:3, :3])
            if theta < -1e5:
                return omega, theta
            ss = skew(omega)
            inv_left_jacobian = (
                np.eye(3) / theta
                - 0.5 * ss
                + (1.0 / theta - 0.5 / np.tan(theta / 2)) * ss @ ss
            )
            v = inv_left_jacobian @ pose[:3, 3]
            return np.concatenate([v, omega]), theta

        self.pinocchio_model.compute_forward_kinematics(qpos)
        ee_index = self.link_name_2_idx[self.move_group]
        current_p = pose7D2mat(self.pinocchio_model.get_link_pose(ee_index))
        target_p = pose7D2mat(target_pose)
        relative_transform = target_p @ np.linalg.inv(current_p)

        omega, theta = pose2exp_coordinate(relative_transform)

        if theta < -1e4:
            return {"status": "screw plan failed."}
        omega = omega.reshape((-1, 1)) * theta

        index = self.move_group_joint_indices
        path = [np.copy(qpos[index])]

        while True:
            self.pinocchio_model.compute_full_jacobian(qpos)
            J = self.pinocchio_model.get_link_jacobian(ee_index, local=False)
            delta_q = np.linalg.pinv(J) @ omega
            delta_q *= qpos_step / (np.linalg.norm(delta_q))
            delta_twist = J @ delta_q

            flag = False
            if np.linalg.norm(delta_twist) > np.linalg.norm(omega):
                ratio = np.linalg.norm(omega) / np.linalg.norm(delta_twist)
                delta_q = delta_q * ratio
                delta_twist = delta_twist * ratio
                flag = True

            qpos += delta_q.reshape(-1)
            omega -= delta_twist

            def check_joint_limit(q):
                n = len(q)
                for i in range(n):
                    if (
                        q[i] < self.joint_limits[i][0] - 1e-3
                        or q[i] > self.joint_limits[i][1] + 1e-3
                    ):
                        return False
                return True

            within_joint_limit = check_joint_limit(qpos)
            self.planning_world.set_qpos_all(qpos[index])
            collide = self.planning_world.collide()

            if (
                np.linalg.norm(delta_twist) < 1e-4
                or collide
                or within_joint_limit == False
            ):
                return {"status": "screw plan failed"}

            path.append(np.copy(qpos[index]))

            if flag:
                if verbose:
                    ta.setup_logging("INFO")
                else:
                    ta.setup_logging("WARNING")
                times, pos, vel, acc, duration = self.TOPP(
                    np.vstack(path), time_step
                )
                return {
                    "status": "Success",
                    "time": times,
                    "position": pos,
                    "velocity": vel,
                    "acceleration": acc,
                    "duration": duration,
                }
