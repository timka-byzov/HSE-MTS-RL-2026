def get_action_value(mdp, state_values, state, action, gamma):
    """ Computes Q(s,a) as in formula above """

    q = 0
    for next_state, ps in mdp.get_next_states(state, action).items():
        r = mdp.get_reward(state, action, next_state)
        q += ps * (r + gamma * state_values[next_state])

    return q
