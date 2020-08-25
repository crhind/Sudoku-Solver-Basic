from game import Game
from typing import Type


    """[Solver class]
    Highest level class, deals with 
    """
class Solver:
    def __init__(self, game: Type[Game]):
        self.game = Game()

        """[]
        Find minimum constrained value
        if potentials = 1 then assign value
        try value 
        
        """
        TODO: Figure out this part.
    def _solve(self) -> bool:
        min_element = min(self.game.elements, key=lambda x: len(x))
        if len(min_element.potentials) == 1:
            min_element.vistied = True
            min_element.value = list(min_element.potentials)[0]
        else:
            for element in self.game.elements:
                element
        
        if (self._solve())

        while (self.game.evaluate()):
            self.next()

    def solve(self):
        self._solve()

        """[Find min constrained value]
        """
    def _next(self):
        min = min(self.game, key=lambda x: len(x))
