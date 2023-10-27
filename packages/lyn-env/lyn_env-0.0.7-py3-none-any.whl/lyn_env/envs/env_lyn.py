import numpy as np
import gym
# import GuiRenBridge
import random
import Cheat
'''

upstream_WL=1.8
downstream_WL=1.5
safe_uWL = 1.5
safe_dWL = 1.3
warn_uWL = 1.4
warn_dWL = 1.4

This file represents a E2E Environment for RL Agent training ,
The dataflow is :Agent -- Action_t --> Environment -- observation_{t+1} , reward_{t+1} --> Agent ...... t is to time of run
'''
def get_random( base , delta):
    return round(base + random.uniform(-delta, delta), 2)


class WaterGateEnv():

    def __init__(self , upstream_WL ,downstream_WL, safe_uWL , safe_dWL , warn_uWL , warn_dWL ):
        self.zeli = Cheat()
        self.upstream_WL = 1.8   #上游水位
        self.downstream_WL = 1.5 #下游水位
        #上下游安全水位
        self.safe_upWL = 1.5
        self.safe_downWL = 1.3
        #上下游警戒水位
        self.warn_upWL = 1.4
        self.warn_downWL = 1.4

        #操作次数
        self.operation_time = 0


    def reset(self):
        self.operation_time = 0

        #todo
        self.upstream_WL = get_random(self.warn_upWL , 0.5 )
        self.downstream_WL = get_random(self.warn_downWL , 0.5 )

        self.flow_rate = 0.0
        return self._get_obs()

    def step(self, action):

        _up , _down = self.zeli.step_action(self.upstream_WL, self.downstream_WL, action)


        # 更新水位高度和流量，根据动作来模拟水闸的调度效果
        if action == 0:  # 关闭水闸
            self.flow_rate = 0.0
        elif action == 1:  # 打开水闸A
            self.flow_rate = 0.2
        else:  # 打开水闸B
            self.flow_rate = -0.1

        self.water_level += self.flow_rate

        reward = self._calculate_reward()
        done = bool(abs(self.water_level - self.target_level) < 0.01)  # 判断是否达到目标水位高度
        info = {}

        return self._get_obs(), reward, done, info

    def _get_obs(self):
        return np.array([self.upstream_WL, self.downstream_WL, self.operation_time])



    def _calculate_reward(self):
        # 计算奖励，设计奖励
        reward = 0
        return reward




