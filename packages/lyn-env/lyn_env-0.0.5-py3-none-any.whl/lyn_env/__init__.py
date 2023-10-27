from gym.envs.registration import register

register(
    id='water_env-v1',
    entry_point='lyn_env.envs:WaterGateEnv',
)
