from Board import Board
from Takuzu import Takuzu


if __name__ == "__main__":  # 

    
    board = Board.read_input('./tests/input/test1.txt')
    
    
    
    
    takuzu = Takuzu(board)
    # print(board.dim)
    # print(board.empty_cells)
    # print(board.row_tally)
    # print(board.col_tally)
    # print(takuzu.actions())
    takuzu.solve()
    # print()
    # print(takuzu.board)
    # f = open("./tests/output/test3.txt", "w")
    # f.write(str(takuzu.path))
    # print(takuzu.path)
    