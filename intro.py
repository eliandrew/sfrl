import gym
import time
from lake_envs import *

env = det_small 
stochastic_env = stochastic_small 

def run(env, max_episodes=1, should_render=True):
	# Every time step t the agent:
	for e in range(max_episodes):
		episode_reward = 0
		t = 0
		done = False
		s = env.reset()
		while not done:
				if should_render:
						env.render()
						time.sleep(0.25)
				action = int(input("Select an action: (0) left, (1) down, (2) right, (3) up\n"))
				(s_prime, r, done, _) = env.step(action)
				input("Took action: {}, received reward: {}, and observation: {}\nPress key to continue.\n".format(action, r, s_prime))
				episode_reward += r
				s = s_prime
				t += 1
