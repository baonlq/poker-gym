from gym.envs.registration import register


register(
    id="poker-v0",
    entry_point="gym_poker.envs:PockerEnv",
    timestep_limit=50)