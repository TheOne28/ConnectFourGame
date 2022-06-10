from enum import Enum

from src.model import State
from src.utility import is_out
import random

streak_way = {
    'HL': (-1, 0), 
    'HR': (1, 0), 
    'VD': (0, -1), 
    'VU': (0, 1), 
    'LD': (-1, -1), 
    'LU': (-1, 1), 
    'RD': (1, -1), 
    'RU': (1, 1)
}


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
        self.findAllPossiblePoint(state)
        
        return random.randint(0, state.board.col)
    


    def findMaximumPoint(self, state : State):
        maximum = -1
        
        for i in range(state.board.row):
            for j in range(state.board.col):

                if(state.board.__getitem__([i, j]).color == self.color):
                    for way in streak_way.keys():
                        score, endPoint = self.findAll(state, i, j, streak_way[way])

                        if(score == 3):
                        
                            pass


                    

    

    def findAll(self, state: State, row: int, col : int, way: tuple):
        current = 0
        endPoint = [[row, col]]


        while(True):
            if(not is_out(row, col) and state.board.__getitem__([row, col]).color == self.color):
                current += 1
                row += way[0]
                col += way[1]
            else:
                endPoint.append([row, col])
                break

        return [current, endPoint]   


    def possibleToAdd(self, state: State, endPoint: list, way: str) -> int:
        before = endPoint[0]
        after = endPoint[1]
        
        optionOne = not is_out(state.board, before[0] - streak_way[way][0], before[1] - streak_way[way][1])
        optionTwo = not is_out(state.board, after[1] + streak_way[way][0], after[1] + streak_way[way][1])

        if(optionOne and optionTwo):
            return 3
        elif(optionOne):
            return 1
        elif(optionTwo):
            return 2
        else:
            return 0