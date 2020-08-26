from typing import *
from element import Element

class Game:
    def __init__(self):
        self._elements = dict()

    @property
    def elements(self) -> Dict[str, Element]:
        return self._elements

    def show_game(self):
        for i in range(1,10):
            for j in range(1,10):
                hold = self.elements["{}{}".format(i,j)]
                print(hold, end=" ")
            print()

    def evaluate(self):
        if any([True for element in self.elements if element.potentials.found]):
            return True
        return False

    '''
    Loads the graph into the game. Doesnt sort out the actual values.
    '''
    def initialise(self, adjList="adjacency_list.txt") -> None:
        with open(adjList, "r") as f:
            lines = f.readlines()
            for line in lines:
                adj = line.split(":")
                element = Element(adj[0])
                element.neighbours = set(adj[1].split(","))
                self.elements[element.id] = element
    
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
            
if __name__ == "__main__":
    game = Game()
    game.initialise()
    game.show_game()

                