from gym.envs.registration import register

register(
    id='water-v1',
    entry_point='lyn_env.envs:WaterGateEnv',
)
