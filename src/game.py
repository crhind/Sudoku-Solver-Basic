from typing import *
from element import Element
from Exceptions import *

import copy

class Game:
    def __init__(self):
        self._elements = dict()

    @property
    def elements(self) -> Dict[str, Element]:
        return self._elements

    def show_game(self):
        for i in range(1,10):
            if i in [4,7]:
                print("- - - + - - - + - - -")
            for j in range(1,10):
                if j in [4,7]:
                    print("|", end=" ")
                hold = self.elements["{}{}".format(i,j)]
                print(hold, end=" ")
            print()
        print("\n")

    def evaluate(self):
        if any([True for element in self.elements if element.potentials.found]):
            return True
        return False

    def initialise(self, adjList="./adjacency_list.txt"):
        with open(adjList, "r") as f:
            lines = f.readlines()
            [self.addElement(line) for line in lines]
        # for k,v in self.elements.items():
        #     print(k, ": ", v.neighbours)
            
    """
    Example.
    54:55,58,59,57,24,34,74,53,14,52,94,84,66,45,46,65,56,44,64,51
    """
    def addElement(self, line: str):
        line = line.rstrip('\r\n')
        entry = line.split(":")
        key_str = entry[0]
        if not key_str in self.elements:
            key = Element(key_str)
            self.elements[key.id] = key
        else: 
            key = self.elements[key_str]

        for neighbour_str in entry[1].split(","):
            if not neighbour_str in self.elements:
                neighbour = Element(neighbour_str)
                self.elements[neighbour.id] = neighbour
            else:
                neighbour = self.elements[neighbour_str]

            key.add_neighbour(neighbour)
            neighbour.add_neighbour(key)
    
    def fillGame(self, url: str) -> None:
        with open(url) as f:
            game_string = f.readline().split(" ")[0]
            for i in range(1,9):
                for j in range(1,9):
                    if not game_string[(i-1) * 9 + j] == "0":
                        key = "{}{}".format(i,j)
                        self.elements[key].assign(int(game_string[(i-1) * 9 + j]))

    def find_mmin(self) -> Type[Element]:
        remaining_elements = [element for _,element in self.elements.items() if not element.visited]
        if any(remaining_elements):
            min_ = min(remaining_elements, key=lambda x: len(x.potentials))
            return min_
        return None

    def find_min(self) -> Type[Element]:
        min_ = 10
        curr = None
        for _ , element in self.elements.items():
            if not element.visited:
                if len(element.potentials) < min_:
                    min_ = len(element.potentials)
                    curr = element
        return curr

    def assign(self, id: str, potential: int):
        self.elements[id].assign(potential)

# TODO: here fix this crap function.
'''
find min
if min
'''
def solve(graph):
	graph.show_game()
	_solve(graph)

def _solve(graph):
    min_ = graph.find_mmin()
    if min_ == None:
        # print("game.py 103: ", min_)
        graph.show_game()
        return True

    if min_.potentials:
        # print("Game.py 107:", min_.id, min_.potentials)
        for potential in min_.potentials:
            new_graph = copy.deepcopy(graph)
            new_graph.assign(min_.id, potential)
            if _solve(new_graph):
                return True
    return False
            
if __name__ == "__main__":
    game = Game()
    game.initialise()
    print("Initialise")
    game.fillGame("./test_game.txt")
    print("fill game")
    print(game.elements)
    game.show_game()
    solve(game)

                