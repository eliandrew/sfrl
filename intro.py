import gym
import time
from envs import *

def print_mdp(P):
	action_map = {
		0: "left",
		1: "down",
		2: "right",
		3: "up"
	}
	for s in P:
		for a in P[s]:
			for (p, s_prime, r, d) in P[s][a]:
				print("s: {}, a: {} s': {}, p: {}, r: {}, d: {}".format(s, action_map[a], s_prime, p, r, d))

def run(env_info, max_episodes=1, should_render=True):
	env, _, _ = env_info
	print_mdp(env.P))
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
