"""Story world"""


class WorldState:
    def __init__(self, time, entities=None, truths=None, lies=None):
        self.time = time
        self.entities = entities if entities else []
        self.truths = truths if truths else set()
        self.lies = lies if lies else set()


class WorldAction:
    def __init__(self, action_specifications, entities_involved, start_state,
            end_state):
        self.action_specifications = action_specifications
        self.entities_involved = entities_involved
        self.start_state = start_state
        self.end_state = end_state


class WorldModel:
    def __init__(self, states=None, actions=None):
        # nodes
        self.states = states if states else []
        # edges
        self.actions = actions if actions else []
