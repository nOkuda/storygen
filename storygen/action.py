class ActionSpecification:
    """Definition of agent action

    name : str
        Identifier for the action.
    entities_involved : [str]
    effects : [(storygen.logic.Proposition, storygen.logic.Proposition, float)]
        The first Proposition contains the preconditions; the second contains
        the postconditions.  The atoms involved in the propositions can be
        simple, non-quantifying predicates applied only to the entities
        specified in ``entities_involved``.  The float is the duration of the
        effect.
    time_to_completion : float
        How long until the action is complete.
    """
    def __init__(self, name, entities_involved, effects, time_to_completion):
        self.name = name
        self.entities_involved = entities_involved
        self.effects = effects
        self.time_to_completion = time_to_completion
