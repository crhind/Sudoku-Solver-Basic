from typing import Set, Type

class Element():
    def __init__(self, id):
        self.neighbours = {}
        self._id = id
        self._potentials = {1,2,3,4,5,6,7,8,9}
        self.value = -1
        self.visited = True

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Type[Element]) -> bool:
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
        if any([True for neighbour in neighbours if value == neighbour.value]):
            return False
        return True

    def remove_potential(self, value: int) -> None:
        if value in self.potentials:
            self.potentials.remove(value)
            print("{} removed as potential from {}".format(value, self.id))

    def assign(self, value: int) -> None:
        if not len(self.potentials) == 1:
            print("Warning: More than 1 potential value")
        self.value = value
        self.visited = True
        for neighbour in self.neighbours:
            neighbour.remove(value)
        
    def __str__(self):
        return "ID: {}, Value: {}, Neighbour: {}".format(self.id, self.value, len(self.neighbours))