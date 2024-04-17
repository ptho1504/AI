
from Board import Board
from Game import Game
from Takuzu import Takuzu
import time


import utils
from copy import deepcopy 




if __name__ == "__main__":  

    # Uncomment to use
    
    board = Board.read_input('./tests/input/test5.txt')
    
    before_memory = utils.get_memory_usage()
    start_time = time.time()
    takuzu = Takuzu(board)
    takuzu.result()
    
    
    end_time = time.time()
    after_memory = utils.get_memory_usage()
    memory_diff = after_memory - before_memory
    print(f"Time execution: {end_time - start_time} seconds")
    print(f"Memory usage: {memory_diff} bytes")
    
    
    print("Ket qua")
    print(takuzu.board)
    print("Path")
    print(takuzu.path)
    
    
    # Uncomment to test Game   
        
    # board = Board.read_input('./tests/input/test5.txt')
    # board_copy = deepcopy(board)
    # takuzu = Takuzu(board)
    # takuzu.result()
    # dim = board.dim
    # path = takuzu.path
    
    # print("Ket qua")
    # print(takuzu.board)
    # print("Path")
    # print(path)
    # game = Game(board_copy, dim, path)
