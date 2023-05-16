from abc import ABC, abstractmethod


class InterfaceUse(ABC):
    @abstractmethod
    def add(self, num1, num2):
        pass
