from Board import Board
from copy import deepcopy
import time

class Takuzu():
    def __init__(self, board: Board):
        self.board = board
        self.path = []
        
    def update(self):
        empty_cells = 0
        row_tally = []
        col_tally = []
        dim = self.board.dim
        for i in range(dim):
            row_tally.append([0, 0])
            col_tally.append([0, 0])
            
        for i in range(dim):
            for j in range(dim):
                val = self.board.array[i][j]
                if val != 2:
                    empty_cells += 1
                    row_tally[i][val] += 1
                    col_tally[j][val] += 1
        
        self.board.row_tally = row_tally
        self.board.col_tally = col_tally
        self.board.empty_cells = dim*dim - empty_cells
    
    def actions(self):
        dim = self.board.dim
        def check_two_numbers(l: int, c: int, v: int):
                for m in ("previous", "following", "below", "above"):
                    f = self.board.two_numbers(l, c, m)
                    if f == (v, v):
                        return False
                return True
            
        def check_adjacent(l: int, c: int, v: int):
            
            hori = self.board.adjacent_horizontal_numbers(l, c)
            vert = self.board.adjacent_vertical_numbers(l, c)
            if hori == (v, v) or vert == (v, v):
                return False
            return True
        
        #Rows and Columns
        #Rows
        row_t = self.board.row_tally
        for i in range(dim):
            zeros = row_t[i][0]
            ones = row_t[i][1]
            # print(zeros,ones)
            # Number of zeros or ones must be = dim/2
            if zeros >= dim / 2 + 1 or ones >= dim / 2 + 1:
                
                return []
            # If only have one cell to filled
            
            
            if zeros + ones == dim - 1:
                p = None
                for j in range(dim):
                    if self.board.get_number(i, j) == 2:
                        p = j #index column need to filled
                if p is None:
                    return []
                
                if zeros - ones != 0:
                    v = 1 if (zeros > ones) else (0)
                    if check_adjacent(i, p, v) and check_two_numbers(
                         i, p, v
                    ):
                        return [(i, p, v)]
                    else:
                        return []
                    
            # If number of ones or number of zeros is maximed
            elif zeros >= dim / 2 or ones >= dim / 2:
                
                for j in range(dim):
                    n = self.board.get_number(i, j)
                    # Find first empty cell
                    if n == 2:
                        # Try assign value
                        v = 1 if (zeros > ones) else (0)
                        # If possible
                        if check_two_numbers(i, j, v) and check_adjacent(
                             i, j, v
                        ):
                            return [(i, j, v)]
                        
                        else:
                            return []
            
        #Columns
        col_t = self.board.col_tally
        for i in range(dim):
            zeros = col_t[i][0]
            ones = col_t[i][1]
            # Number of zeros or ones must be = dim/2
            if zeros >= dim / 2 + 1 or ones >= dim / 2 + 1:
                return []
            
            if zeros + ones == dim - 1:
                p = None
                for j in range(dim):
                    if self.board.get_number(j, i) == 2:
                        p = j
                if p is None:
                    return []
                if zeros - ones != 0:
                    v = 1 if (zeros > ones) else (0)
                    if check_adjacent( p, i, v) and check_two_numbers(
                         p, i, v
                    ):
                        return [(p, i, v)]
                    else:
                        return []   
                

            # If number of ones or number of zeros is maximed
            elif zeros >= dim / 2 or ones >= dim / 2:
                for j in range(dim):
                    n = self.board.get_number(j, i)
                    # # Find first empty cell
                    if n == 2:
                        # Tentar atribuir-lhe o valor em menor número
                        v = 1 if (zeros > ones) else (0)
                        # Try assign value
                        if check_two_numbers( j, i, v) and check_adjacent(
                             j, i, v
                        ):
                            return [(j, i, v)]
                        # If possible
                        else:
                            return []

        # 02. Case in which we have 2 consecutive cells that are the same
        modes = ("previous", "following", "below", "above")
        for i in range(dim):
            for j in range(dim):
                if self.board.get_number(i, j) == 2:
                    for m in modes:
                        t = self.board.two_numbers(i, j, m)
                        if t == (0, 0):
                            return [(i, j, 1)]
                        elif t == (1, 1):
                            return [(i, j, 0)]

        # 03. Case in which we see the immediately adjacent cells
        for i in range(dim):
            for j in range(dim):
                if self.board.get_number(i, j) == 2:
                    h = self.board.adjacent_horizontal_numbers(i, j)
                    v = self.board.adjacent_vertical_numbers(i, j)
                    
                    if h == (0, 0) or v == (0, 0):
                        return [(i, j, 1)]
                    if h == (1, 1) or v == (1, 1):
                        return [(i, j, 0)]

        # 04. Case in which we know nothing and give priority to the number least present in the row and column
        res = []
        for i in range(dim):
            for j in range(dim):
                if self.board.get_number(i, j) == 2:
                    if (row_t[i][0] > row_t[i][1] and col_t[j][0] >= col_t[j][1]) or (
                        row_t[i][0] >= row_t[i][1] and col_t[j][0] > col_t[j][1]
                    ):
                        return [(i, j, 1), (i, j, 0)]
                    elif (row_t[i][0] < row_t[i][1] and col_t[j][0] <= col_t[j][1]) or (
                        row_t[i][0] <= row_t[i][1] and col_t[j][0] < col_t[j][1]
                    ):
                        return [(i, j, 0), (i, j, 1)]
                    else:
                        return [(i, j, 0), (i, j, 1)]
        return res
    
    def is_valid_move(self, x, y, v):
        # Check if the cell is empty
        if self.board.get_number(x, y) != 2:
            return False
        
        # Check if the move violates the rule of not having three consecutive numbers
        for m in ("previous", "following", "below", "above"):
            f = self.board.two_numbers(x, y, m)
            if f == (v, v):
                return False
        
        # Check if the move violates the rule of adjacent horizontal and vertical numbers
        hori = self.board.adjacent_horizontal_numbers(x, y)
        vert = self.board.adjacent_vertical_numbers(x, y)
        
        if hori == (v, v) or vert == (v, v):
            return False
        
        return True
    
    def heuristic_empty_cells(self):
        empty_cells = 0
        for i in range(self.board.dim):
            for j in range(self.board.dim):
                if self.board.get_number(i, j) == 2:  # 2 represents an empty cell
                    if self.is_valid_move(i, j, 0) or self.is_valid_move(i, j, 1):
                        empty_cells += 1
        return empty_cells
    
    def heuristic_consistency_diversity(self):
        row_diff = sum(abs(row[0] - row[1]) for row in self.board.row_tally)
        col_diff = sum(abs(col[0] - col[1]) for col in self.board.col_tally)
        return row_diff + col_diff
    
    def heuristic(self):
        return self.heuristic_empty_cells() + self.heuristic_consistency_diversity()
    
    def actions_sorted_by_heuristic(self):
        actions = self.actions()
        # if len(actions) > 1:
        #     for action in actions:
        #         print ("diem", self.apply_heuristic(action))
        return sorted(actions, key=lambda action: self.apply_heuristic(action))
    
    def apply_heuristic(self, action):
        # new_board = self.apply_actions([action])
        return self.heuristic()
    
    
    def apply_actions(self, actions):
        new_board = deepcopy(self.board)
        for action in actions:
            x, y, v = action
            new_board.array[x][y] = v

        return new_board
    
    # def result(self):
    #     start_time = time.time()
    #     if self.goal_test():
    #         return True
        
    #     actions = self.actions()
        
    #     for action in actions:
    #         x,y,v = action
    #         self.board.array[x][y] = v
    #         self.update()
    #         # print(action)
    #         # print(self.board)
    #         if self.result():
    #             self.path.append(action)
    #             end_time = time.time()
    #             # print(f"Time execution: {end_time - start_time} seconds")
    #             return True
            
    #         self.board.array[x][y] = 2
    #         self.update()
    #     # end_time = time.time()
    #     # print(f"Time execution: {end_time - start_time} seconds")
    #     return False
    
    def result(self):
        
        if self.goal_test():
            return True
        
        actions = self.actions_sorted_by_heuristic()
        
        for action in actions:
            
            x, y, v = action
            self.board.array[x][y] = v
            self.update()
            
            # print(self.board)
            # print("")
            if self.result():
                self.path.append(action)
                
                return True
                
            self.board.array[x][y] = 2
            self.update()
        
        return False
            
    
    def goal_test(self):
    
        board = self.board
        row_t = board.row_tally
        col_t = board.col_tally
        dim = board.dim
        
        # print(row_t)
        #Check sum of number 0s and number 1s in one row == dim
        for i in range(dim):
            if sum(row_t[i]) != dim:
                return False
        rows = set()
        cols = set()
        for i in range(dim):
            r = board.get_row(i)
            c = board.get_column(i)
            if r in rows or c in cols:
                return False
            else:
                if (
                    row_t[i][0] >= dim / 2 + 1
                    or row_t[i][1] >= dim / 2 + 1
                    or col_t[i][0] >= dim / 2 + 1
                    or col_t[i][1] >= dim / 2 + 1
                ):
                    return False
                rows.add(r)
                cols.add(c)
        return True
    
    