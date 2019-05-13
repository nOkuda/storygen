"""Kleene Logic"""


# https://gist.github.com/gvx/2185287
class Formula:
    def __invert__(self):
        return Not(self)

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __rshift__(self, other):
        return Implies(self, other)

    def __lshift__(self, other):
        return Iff(self, other)


class BinOp(Formula):
    def __init__(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '(' + str(self.lchild) + ' ' + self.op+ ' ' + str(self.rchild) + ')'


class And(BinOp):
    op = '∧'


class Or(BinOp):
    op = '∨'


class Implies(BinOp):
    op = '→'


class Iff(BinOp):
    op = '↔'


class Not(Formula):
    def __init__(self, child):
        self.child = child

    def v(self, v):
        return ~self.child.v(v)

    def __str__(self):
        return '¬' + str(self.child)


class Atom(Formula):
    """Intended as a placeholder for a simple, non-quantifying predicate"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


def evaluate(proposition, truths, lies):
    """Return truth value of this proposition according to the given state
    using Kleene logic

    proposition : storygen.logic.Formula
    state : storygen.world.WorldState
    """
    pass


def lukasiewicz_evaluate(proposition, state):
    """Return truth value of this proposition according to the given state
    using Łukasiewicz logic

    proposition : storygen.logic.Formula
    state : storygen.world.WorldState
    """
    pass

