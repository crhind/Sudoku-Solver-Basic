from Typing import *
from element import Element

class Game:
    def __init__(self):
        self.elements = {}

    @property
    def elements(self) -> Dict[Element]:
        return self._neighbours

    def show_game(self):
        for i in range(1,9):
            for j in range(1,9):
                print(self.elements["{}{}".format(i,j)],end=" ")
            print()

    def evaluate(self):
        if any([True for element in self.elements if element.potentials.found])
            return True
        return False

    def initialise(self) -> None:
        for i in range(1,9):
            for j in range(1,9):
                element = Element("{}{}".format(i,j))
                self.elements[node.id] = elemment
    
    def fillGame(self, url: str) -> None:
        with open(url) as f:
            game_string = f.readline().split(" ")[0]
            for i in range(1,9):
                for j in range(1,9):
                    if not game_string[(i-1) * 9 + j] is "0":
                        self.elements["{}{}".format(i,j)].value = game_string[(i-1) * 9 + j]
                        self.elements["{}{}".format(i,j)].potentials = {}

    def find_mmin(self) -> Type[Element]:
        return min(self.elements, key=lambda x: len(x.potentials))

    def find_min(self) -> Type[Element]:
        min_ = 10
        curr = None
        for element in self.elements:
            if not element.assigned:
                if len(element.potentials) < min_:
                    min_ = len(element.potentials)
                    curr = element
        return curr

# TODO: here fix this crap function.
'''
find min
if min
'''
    def solve(graph: Type[Game]):
        min_element = graph.find_min()
        if not min_element:        
            graph.show_game()
            return
        else:
            for potential in min_element.potentials:
                min_element.assign(potential)
                solve(graph)
            

                