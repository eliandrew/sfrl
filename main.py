import gym
import time
from value_iteration import *
from envs import *

def solve(
	env_info, 
	gamma=0.9, 
	delta=0.001, 
	n_episodes=1, 
	should_render=True, 
	should_pause=False, 
	verbose=True):
	env, n, m = env_info
	# Solve the MDP of the given environment using value iteration	
	v_opt = value_iteration(env.P)
	display_values(v_opt, n, m)

	pi_opt = greedy_policy(env.P, v_opt)
	display_values(pi_opt, n, m)

	total_reward = 0

	for e in range(n_episodes):
		episode_reward = 0
		t = 0
		done = False
		s = env.reset()
		while not done:
				if should_render:
						env.render()
						time.sleep(0.25)
				action = pi_opt[s]
				(s_prime, r, done, _) = env.step(action)
				if verbose:
					print("Took action: {}, received reward: {}, and observation: {}\n".format(action, r, s_prime))
				if should_pause:
					input("Press key to continue.\n")
				episode_reward += r
				s = s_prime
				t += 1

				total_reward += episode_reward
		print("Completed episode {} in {} timesteps with {} reward".format(e, t, episode_reward))

	print("Completed {} episodes with {} average reward and {} total reward".format(
			int(n_episodes), total_reward / float(n_episodes), total_reward))

