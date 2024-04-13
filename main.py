from Board import Board
from Takuzu import Takuzu


if __name__ == "__main__":  # Função main

    # Resolução do problema
    # board = Board([
    #         [2, 2, 0, 1],
    #         [1, 0, 2, 1],
    #         [0, 2, 1, 0],
    #         [1, 2, 2, 2]
    # ],4,9, [[1,1],[1,2],[2,1],[0,1]], [[1,2],[1,0],[1,1],1,2])
    board = Board([
            [2,2,2,0,2,0],
            [1,2,2,0,2,2],
            [1,2,2,2,1,2],
            [2,2,1,2,2,2],
            [2,0,2,2,2,2],
            [2,2,2,2,2,2],
    ],6,8, [[2,0],[1,1],[0,2],[0,1],[1,0],[0,0]], [[0,2],[1,0],[0,1],[2,0],[0,1],[1,0]])
    
    takuzu = Takuzu(board)
    # print(takuzu.actions())
    takuzu.result()
    print()
    print(takuzu.board)
    print(takuzu.path)
    