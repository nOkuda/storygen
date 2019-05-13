class Value:
    def __init__(self):
        raise NotImplementedError('Truth value not meant to be instantiated')


class TrueValue(Value):
    def __init__(self):
        super().__init__(self)


class FalseValue(Value):
    def __init__(self):
        super().__init__(self)


class UnknownValue(Value):
    def __init__(self):
        super().__init__(self)
