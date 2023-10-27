
class GR_test:
    def step_action(upstream_WL, downstream_WL, action):

        _upstream_WL = upstream_WL * action + 0.2
        _downstream_WL = downstream_WL * action + 0.1
        return  _upstream_WL, _downstream_WL
