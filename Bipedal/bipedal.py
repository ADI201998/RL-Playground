import gym
import numpy as np
import random
import Box2D

env = gym.make("BipedalWalkerHardcore-v3").env
env.reset()
print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

#min_pos = -1.2,	max_pos = 0.6
#min_vel = -0.07,	max_vel = 0.07
q_table = np.zeros((19, 15, 3))

alpha = 0.1
gamma = 0.6
epsilon = 0.1
state = env.reset()
print("Starting Training")
for i in range(1, 100001):
    action = env.action_space.sample()
    #print(action)
    env.render()
    #print("State : ", state.size)
	

print("Training finished.\n")
env.close()
