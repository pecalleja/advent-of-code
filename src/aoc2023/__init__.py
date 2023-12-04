import inspect
import os
from abc import ABC
from abc import abstractmethod


class Solution(ABC):
    def __init__(self, data):
        self.data = [x.strip() for x in data.splitlines() if x.strip()]

    @abstractmethod
    def result(self):
        raise NotImplementedError

    @classmethod
    def from_file(cls, filename=None):
        if filename is None:
            class_file = inspect.getfile(cls)
            this_dir = os.path.dirname(class_file)
            filename = os.path.join(this_dir, "input.txt")
        with open(filename) as f:
            data = f.read()
            return cls(data)
