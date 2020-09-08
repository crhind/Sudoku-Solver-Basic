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
            if i in [4,7]:
                print("- - - + - - - + - - -")
            for j in range(1,10):
                if j in [4,7]:
                    print("|", end=" ")
                hold = self.elements["{}{}".format(i,j)]
                print(hold, end=" ")
            print()

    def evaluate(self):
        if any([True for element in self.elements if element.potentials.found]):
            return True
        return False

    def initialise(self, adjList="./adjacency_list.txt"):
        with open(adjList, "r") as f:
            lines = f.readlines()
            [self.addElement(line) for line in lines]
            
            # for line in lines:
            #	self.addElement(line)

    def addElement(self, line: str):
        entry = line.split(":")
        key_str = entry[0]
        if not key_str in self.elements:
            self.elements[key_str] = Element(key_str)

        for neighbour_str in entry[1].split(","):
            if not neighbour_str in self.elements:
                neighbour=Element(neighbour_str)
                self.elements[neighbour.id] = neighbour
                self.elements[key_str].add_neighbour(neighbour)
                neighbour.add_neighbour(self.elements[key_str])

    # '''
    # Loads the graph into the game. Doesnt sort out the actual values.
    # '''
    # def initialise(self, adjList="adjacency_list.txt") -> None:
    #     with open(adjList, "r") as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             adj = line.split(":")
    #             element = Element(adj[0])
    #             for key in adj[1].split(","):
    #                 if key in self.elements:
    #                     element.add_neighbours = self.elements[key]
    #                 else:
    #                     element.add_neighbours = Element(key)
    #             self.elements[element.id] = element
    
    def fillGame(self, url: str) -> None:
        with open(url) as f:
            game_string = f.readline().split(" ")[0]
            for i in range(1,9):
                for j in range(1,9):
                    if not game_string[(i-1) * 9 + j] == "0":
                        key = "{}{}".format(i,j)
                        self.elements[key].assign(game_string[(i-1) * 9 + j])

    def find_mmin(self) -> Type[Element]:
        return min(self.elements, key=lambda x: len(x.potentials))

    def find_min(self) -> Type[Element]:
        min_ = 10
        curr = None
        for _ , element in self.elements.items():
            if not element.visited:
                if len(element.potentials) < min_:
                    min_ = len(element.potentials)
                    curr = element
        return curr

# TODO: here fix this crap function.
'''
find min
if min
'''
def solve(graph):
	graph.show_game()
	_solve(graph)
	graph.show_game()

def _solve(graph):
	min_ = graph.find_min()
	if not min_:
		return
	for potential in min_.potentials:
		min_.assign(potential)
		solve(graph)
            
if __name__ == "__main__":
    game = Game()
    game.initialise()
    print(game.elements)
    game.fillGame("./test_game.txt")
    game.show_game()
    solve(game)

                