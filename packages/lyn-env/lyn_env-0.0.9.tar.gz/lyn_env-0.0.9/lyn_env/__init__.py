from gym.envs.registration import register

register(
    id='Water_g-v1',
    entry_point='lyn_env.envs:WaterGateEnv',
    kwargs={'upstream_WL': 1.8, 'downstream_WL': 1.8, 'safe_uWL': 1.3, 'safe_dWL': 1.4, 'warn_uWL': 1.5, 'warn_dWL': 1.5},
)
