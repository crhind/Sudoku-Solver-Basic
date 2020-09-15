from typing import Set, Type
from Exceptions import *

class Element():
    def __init__(self, id):
        self.neighbours = {}
        self._id = id
        self._potentials = {1,2,3,4,5,6,7,8,9}
        self.value = 0
        self.visited = False

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: 'Element') -> bool:
        if other == None:
            return False
        if self.id == other.id:
            return True
        return False

    @property
    def id(self) -> str:
        return self._id

    @property
    def potentials(self) -> Set:
        return self._potentials

    @property
    def found(self) -> bool:
        return self.found
    
    def contains(self, value: int) -> bool:
        if any([True for neighbour in self.neighbours if value == neighbour.value]):
            return False
        return True

    def remove_potential(self, value: int) -> bool:
        if value in self.potentials:
            self.potentials.remove(value)
            # print("\t{} removed as potential from {}".format(value, self.id))
            # if len(self.potentials) == 1:
            #     print("element.py 44:", self.id, value)
            #     self.assign(list(self.potentials)[0])
            return True
        return False

    def assign(self, value: int) -> None:
        # if self.visited:
        #     print("major fuck up here")

        # if not value in self.potentials:
        #     print("Exception caught: attempted assigned value:", value ,self.__repr__())
            # raise NotAssignableException("Cannot assign value that is not in elements potential values.")

        self.value = value
        self.visited = True
        self._potentials = {}
        # print("assigning {} to ID: {}".format(value, self.id))
        for _ , neighbour in self.neighbours.items():
            neighbour.remove_potential(value)
        return True

    def add_neighbour(self, neighbour: 'Element') -> None:
        self.neighbours[neighbour.id] = neighbour
        
    def __repr__(self):
        return "ID: {}, Value: {}, Potentials {}, Neighbour: {}\n".format(self.id, self.value, self.potentials, len(self.neighbours))

    def __str__(self):
        return "{}".format(self.value)