# sfrl
Salesforce RL Intro

To get started run:

`conda create -f environment.yml` to create your conda environment

and then:

`conda activate salesforce-rl` to activate the environment


- `intro.py`: Short intro to OpenAI Gym environments and API

Run `run(det_small)` to see a walk through of the OpenAI Gym API for the 4x4 Deterministic FrozenLake Environment
Run `run(stochastic_small)` to see a walk through of the OpenAI Gym API for the 4x4 Stochastic FrozenLake Environment 

- `envs.py`: Defines the environments we will be using


- `main.py`: Defines a `run` function to test our value iteration on any environment


- `value_iteration.py`: Empty implementations of value iteration functions


- `answers/value_iteration_answers.py`: Implementations of value iteration functions