from os import stat
from src.model import State
import random

class Bot13520099:
    def __init__(self) -> None:
        pass

    def find(self, state: State, player: int, thinking_time: float) -> int:
        """
        [DESC]
            Function to find the best move for player
        [PARAMS]
            state: State -> current state
            player: int -> player to find the best move
            thinking_time: float -> time limit for bot to find the best move
        [RETURN]
            int -> column to place piece
        """
        # Implement greedy algorithm here
        # ...
        
        self.color = state.players[player].color
        
        


        return random.randint(0, state.board.col)

    def posibbleAdded(self, state: State, row : int, col:int) -> bool:
        return row < 0 or col < 0 or row >= state.board.row or col >= state.board.col 
    
    def findAllPossiblePoint(self, state : State, color: str):
        donePoint = []

        for i in range(state.board.row):
            for j in range(state.board.col):

                if(state.board.__getitem__([i, j]) == color):
                    donePoint.append([i, j])
                    
            