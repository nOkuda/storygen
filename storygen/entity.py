"""Entities"""
import uuid

from storygen.world import WorldModel


class Entity:
    def __init__(self, name):
        self.identifier = uuid.uuid4()
        self.name = name
        self.goals = []
        self.inner_model = WorldModel()
