
from Board import Board
from Game import Game
from Takuzu import Takuzu
import time


import utils
from copy import deepcopy 




if __name__ == "__main__":  

    # board = Board.read_input('./tests/input/test5.txt')
    
    # before_memory = utils.get_memory_usage()
    # # print(before_memory)
    # start_time = time.time()
    # takuzu = Takuzu(board)
    # # board_copy = deepcopy(board)
    # # print(start_time)
    # takuzu.result()
    
    
    # end_time = time.time()
    # after_memory = utils.get_memory_usage()
    # # print(end_time)
    # # print(after_memory)
    # memory_diff = after_memory - before_memory
    # print(f"Time execution: {end_time - start_time} seconds")
    # print(f"Memory usage: {memory_diff} bytes")
    # i = 1
    # f = open('./tests/output/test'+ str(i)+'.txt', "w")
    # f.write(str(takuzu.board))
    
    # print("Ket qua")
    # print(takuzu.board)
    # print("Path")
    # print(takuzu.path)
    # Gameee
    
    # takuzu.result()
    # dim = board.dim
    # path = takuzu.path
    # game = Game(board_copy, dim, path)
    # for i in range (1, 10+1):
    #     board = Board.read_input('./tests/input/test'+ str(i)+'.txt')
    
    
    #     # start = time.time()
    #     takuzu = Takuzu(board)
    #     takuzu.result()
    #     # end = time.time()
    #     # print(end - start)
    #     f = open('./tests/output/test'+ str(i)+'.txt', "w")
    #     f.write(str(takuzu.board))
    
    
        
    board = Board.read_input('./tests/input/test5.txt')
    board_copy = deepcopy(board)
    takuzu = Takuzu(board)
    takuzu.result()
    dim = board.dim
    path = takuzu.path
    
    print("Ket qua")
    print(takuzu.board)
    print("Path")
    print(path)
    game = Game(board_copy, dim, path)
