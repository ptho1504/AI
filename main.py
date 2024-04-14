import psutil
from Board import Board
from Takuzu import Takuzu
import time

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss

if __name__ == "__main__":  # 

    board = Board.read_input('./tests/input/test1.txt')
    
    before_memory = get_memory_usage()
    # print(before_memory)
    start_time = time.time()
    takuzu = Takuzu(board)
    # print(start_time)
    takuzu.result()
    
    
    end_time = time.time()
    after_memory = get_memory_usage()
    # print(end_time)
    # print(after_memory)
    memory_diff = after_memory - before_memory
    print(f"Time execution1: {end_time - start_time} seconds")
    print(f"Memory usage: {memory_diff} bytes")
    
    
    # print("")
    # print(takuzu.board)
    # print(takuzu.path)
    
    # for i in range (1, 10+1):
    #     board = Board.read_input('./tests/input/test'+ str(i)+'.txt')
    
    
    #     # start = time.time()
    #     takuzu = Takuzu(board)
    #     takuzu.result()
    #     # end = time.time()
    #     # print(end - start)
    #     f = open('./tests/output/test'+ str(i)+'.txt', "w")
    #     f.write(str(takuzu.board))
    
    