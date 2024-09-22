from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        
    @property
    @abstractmethod
    def name(self):...



class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name): 
        self._name = name


foo = Foo('Bar')
print(foo.name)