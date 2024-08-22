from omni.isaac.lab.utils import configclass

from .rough_env_cfg import UnitreeGo2RoughEnvCfg



@configclass
class UnitreeGo2FlatEnvCfg(UnitreeGo2RoughEnvCfg):
    def __post_init__(self):
        # Temporarily not run disable_zerow_eight_rewards() in parent class to override rewards
        self._run_disable_zero_weight_rewards = False    ## 暂时不在父类中运行disable_zerow_eight_rewards()方法，以便重写奖励
        # post init of parent
        super().__post_init__()

        # override rewards     重写奖励参数
        self.rewards.flat_orientation_l2.weight = -2.5   #偏离水平姿态的惩罚，变得更大
        self.rewards.feet_air_time.weight = 0.25         #脚在空中的时间奖励。正权重表明希望鼓励跳跃或步态轻快
        
        self.rewards.base_height_l2.weight = -2          #机器人基座高度的惩罚
        self.rewards.base_height_rough_l2.weight = 0     #粗糙地面为0
        # change terrain to flat
        self.scene.terrain.terrain_type = "plane"    #改变地形
        self.scene.terrain.terrain_generator = None   #设置策略中的高度扫描为None
        # no height scan
        self.scene.height_scanner = None     #置高度扫描器为None，表示不进行高度扫描
        self.observations.policy.height_scan = None
        # no terrain curriculum
        self.curriculum.terrain_levels = None   #无课程学习

        # Now executing disable_zerow_eight_rewards()  现在执行disable_zerow_eight_rewards()
        self._run_disable_zero_weight_rewards = True
        if self._run_disable_zero_weight_rewards:
            self.disable_zero_weight_rewards()
