import numpy as np

def greedy_policy(P, V):
    """Returns a new policy by action greedily on the given
    value function V.

    Policy is a dict: (state) => action
    """
    return {s: np.argmax([action_value(P, s, a, V) for a in P[s]]) for s in P}

def value_iteration(P, gamma=0.9, delta=0.001):
    """Performs value iteration on the given MDP.

    Until convergence, update each state using the value iteration
    step.
    """
    k = 0
    v_opt = {s: 0.0 for s in P}

    max_delta = delta

    while max_delta >= delta:
        v_k = {s: value_iteration_step(P, s, v_opt, gamma) for s in P}
        max_delta = max([abs(v_k[s] - v_opt[s]) for s in P])
        v_opt = v_k
        k += 1

    print("Finished value iteration in {} time steps.".format(k))

    return v_opt

def value_iteration_step(P, s, v_k, gamma=0.9):
    """Performs a single step of the value iteration algorithm.

    $v_{k+1}(s) = max_{a in A}(sum_{s' in S}P_{ss'}^a(R_a^s + gamma * v_k(s')))$
    """

    return max([action_value(P, s, a, v_k, gamma) for a in P[s]])

def action_value(P, s, a, v_k, gamma=0.9):
    """Calculates the value of the given action.

    $sum_{s' in S}P_{ss'}^a(R_a^s + gamma * v_k(s'))$
    """

    return sum([prob * (r + gamma * v_k[s_prime]) for (prob, s_prime, r, done) in P[s][a]])

def display_values(v, n, m):
    """Displays the values in v on an nxm grid.
    """
    grid = np.array([v[s] for s in v]).reshape(n, m)
    print(grid)