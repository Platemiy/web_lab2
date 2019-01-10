from abc import ABCMeta, abstractmethod
class Figure(object):
    __metaclass__ = ABCMeta
    @staticmethod
    @abstractmethod
    def area(self):
        pass