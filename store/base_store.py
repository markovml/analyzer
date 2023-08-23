from abc import ABC, abstractmethod

class BaseStore(ABC):
    def __init__(self):
        self.class_type = ""

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self):
        pass

    @abstractmethod
    def update(self):
        pass
