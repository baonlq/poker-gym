import gym
import gym_pull

gym_pull.pull('github.com/baonlq/poker-gym')
env = gym.make('baonlq/poker-v0')
env.reset()
