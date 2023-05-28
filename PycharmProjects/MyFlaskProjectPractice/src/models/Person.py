from dataclasses import dataclass


@dataclass
class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self.health = 100

    def __repr__(self):
        return "the name is " + self._name


