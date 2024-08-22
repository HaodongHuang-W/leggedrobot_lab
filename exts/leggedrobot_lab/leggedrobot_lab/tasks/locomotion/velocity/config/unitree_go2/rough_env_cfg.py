from robot_lab.tasks.locomotion.velocity.velocity_env_cfg import LocomotionVelocityRoughEnvCfg

from omni.isaac.lab.utils import configclass

##
# Pre-defined configs
##
# use cloud assets
from omni.isaac.lab_assets.unitree import UNITREE_GO2_CFG

@configclass
class UnitreeGo2RoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # ------------------------------Sence------------------------------
        # switch robot to unitree-a1
        self.scene.robot = UNITREE_GO2_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.scene.height_scanner.prim_path = "{ENV_REGEX_NS}/Robot/base"
        # scale down the terrains because the robot is small
        self.scene.terrain.terrain_generator.sub_terrains["boxes"].grid_height_range = (0.025, 0.1)
        self.scene.terrain.terrain_generator.sub_terrains["random_rough"].noise_range = (0.01, 0.06)
        self.scene.terrain.terrain_generator.sub_terrains["random_rough"].noise_step = 0.01

        # ------------------------------Actions------------------------------
        # reduce action scale
        self.actions.joint_pos.scale = 0.25
        self.actions.joint_pos.clip = {".*": (-100, 100)}

        # ------------------------------Events------------------------------
        self.events.push_robot = None
        self.events.add_base_mass.params["mass_distribution_params"] = (-1.0, 3.0)
        self.events.add_base_mass.params["asset_cfg"].body_names = ["base"]
        self.events.base_external_force_torque.params["asset_cfg"].body_names = ["base"]
        self.events.reset_robot_joints.params["position_range"] = (1.0, 1.0)
        self.events.reset_base.params = {
            "pose_range": {"x": (-0.5, 0.5), "y": (-0.5, 0.5), "yaw": (-3.14, 3.14)},
            "velocity_range": {
                "x": (-0.5, 0.5),
                "y": (-0.5, 0.5),
                "z": (-0.5, 0.5),
                "roll": (-0.5, 0.5),
                "pitch": (-0.5, 0.5),
                "yaw": (-0.5, 0.5),
            },
        }
        self.events.randomize_actuator_gains = None
        self.events.randomize_joint_parameters = None

        # ------------------------------Rewards------------------------------
        # General
        # UNUESD self.rewards.is_alive.weight = 0
        self.rewards.is_terminated.weight = 0

        # Root penalities
        self.rewards.lin_vel_z_l2.weight = -2.0          #z轴的线速度
        self.rewards.ang_vel_xy_l2.weight = -0.05        #在XY平面上的角速度惩罚
        self.rewards.flat_orientation_l2.weight = -0.5   #保持水平
        self.rewards.base_height_l2.weight = 0           #base的高度，不使用
        self.rewards.base_height_l2.params["target_height"] = 0.35  #base目标高度
        self.rewards.base_height_l2.params["asset_cfg"].body_names = ["base"]
        self.rewards.body_lin_acc_l2.weight = 0         #线加速度，不使用
        self.rewards.body_lin_acc_l2.params["asset_cfg"].body_names = ["base"]  #base的线加速度

        #Joint penalties
        self.rewards.joint_torques_l2.weight = -0.0002  #不希望关节力矩太大
        self.rewards.joint_vel_l2.weight = 0            #表示不使用
        self.rewards.joint_acc_l2.weight = -2.5e-7     #关节加速度
        self.rewards.joint_pos_limits.weight = -5.0   #关节位置超限的惩罚
        self.rewards.joint_vel_limits.weight = 0

        #Action penalties
        self.rewards.applied_torque_limits.weight = 0
        self.rewards.applied_torque_limits.params["asset_cfg"].body_names = ["base"]
        self.rewards.action_rate_l2.weight = -0.01      #负权重表明惩罚过快的动作变化，鼓励平滑的动作

        # Contact sensor
        self.rewards.undesired_contacts.weight = -1.0   #不期望接触的惩罚
        self.rewards.undesired_contacts.params["sensor_cfg"].body_names = [".*_thigh"]  #将不期望接触的惩罚应用于所有与"thigh"（大腿）相关的身体部分
        self.rewards.contact_forces.weight = 0  #接触力，设置为0
        self.rewards.contact_forces.params["sensor_cfg"].body_names = [".*_foot"]  #接触力适用于所有的脚

        #Velocity-tracking rewards
        self.rewards.track_lin_vel_xy_exp.weight = 1.5   #xy上的线速度
        self.rewards.track_ang_vel_z_exp.weight = 0.75   #在Z轴上跟踪角速度的奖励

        #Others
        self.rewards.feet_air_time.weight = 0.01
        self.rewards.feet_air_time.params["sensor_cfg"].body_names = [".*_foot"]
        self.rewards.foot_contact.weight = 0
        self.rewards.foot_contact.params["sensor_cfg"].body_names = [".*_foot"]
        self.rewards.base_height_rough_l2.weight = 0
        self.rewards.base_height_rough_l2.params["target_height"] = 0.35
        self.rewards.base_height_rough_l2.params["asset_cfg"].body_names = ["base"]
        self.rewards.feet_slide.weight = 0
        self.rewards.feet_slide.params["sensor_cfg"].body_names = [".*_foot"]
        self.rewards.feet_slide.params["asset_cfg"].body_names = [".*foot"]
        self.rewards.joint_power.weight = -2e-5
        self.rewards.stand_still_when_zero_command.weight = -0.5 #静止时希望不要动

        # If the weight of rewards is 0, set rewards to None
        if self._run_disable_zero_weight_rewards:
            self.disable_zero_weight_rewards()

        # ------------------------------Terminations------------------------------
        self.terminations.illegal_contact.params["sensor_cfg"].body_names = ["base"]

        # ------------------------------Commands------------------------------




  













        # self.rewards.feet_air_time.params["sensor_cfg"].body_names = ".*_foot"
        # self.rewards.feet_air_time.weight = 0.01
        # self.rewards.undesired_contacts = None
        # self.rewards.dof_torques_l2.weight = -0.0002
        # self.rewards.track_lin_vel_xy_exp.weight = 1.5
        # self.rewards.track_ang_vel_z_exp.weight = 0.75
        # self.rewards.dof_acc_l2.weight = -2.5e-7

        # # terminations
        # self.terminations.base_contact.params["sensor_cfg"].body_names = "base"


# @configclass
# class UnitreeGo2RoughEnvCfg_PLAY(UnitreeGo2RoughEnvCfg):
#     def __post_init__(self):
#         # post init of parent
#         super().__post_init__()

#         # make a smaller scene for play
#         self.scene.num_envs = 50
#         self.scene.env_spacing = 2.5
#         # spawn the robot randomly in the grid (instead of their terrain levels)
#         self.scene.terrain.max_init_terrain_level = None
#         # reduce the number of terrains to save memory
#         if self.scene.terrain.terrain_generator is not None:
#             self.scene.terrain.terrain_generator.num_rows = 5
#             self.scene.terrain.terrain_generator.num_cols = 5
#             self.scene.terrain.terrain_generator.curriculum = False

#         # disable randomization for play
#         self.observations.policy.enable_corruption = False
#         # remove random pushing event
#         self.events.base_external_force_torque = None
#         self.events.push_robot = None