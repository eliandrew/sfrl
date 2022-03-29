"""Defines some frozen lake maps."""
import gym
from gym.envs.toy_text import frozen_lake
from gym.envs.registration import register


register(
    id='Deterministic-4x4-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': False})

register(
    id='Deterministic-8x8-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '8x8',
            'is_slippery': False})

register(
    id='Stochastic-4x4-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': True})

register(
    id='Stochastic-8x8-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '8x8',
            'is_slippery': True})


det_small = (gym.make('Deterministic-4x4-FrozenLake-v0'), 4, 4)
det_large = (gym.make('Deterministic-8x8-FrozenLake-v0'), 8, 8)
stochastic_small = (gym.make('Stochastic-4x4-FrozenLake-v0'), 4, 4)
stochastic_large = (gym.make('Stochastic-8x8-FrozenLake-v0'), 8, 8)