from Board import Board


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
        self.board.empty_cells = empty_cells
    
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
                p = 0
                for j in range(dim):
                    if self.board.get_number(i, j) == 2:
                        p = j #index column need to filled
                
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
                p = 0
                for j in range(dim):
                    if self.board.get_number(j, i) == 2:
                        p = j
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
                    # Se houver alguma dupla igual, a escolha é óbvia
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
    
     
    
    def result(self):
        while self.goal_test() == False:
           if(self.actions() != []):
            #    print("self.action", self.actions())
               actions = self.actions()
               self.path.append(actions)
            #    print("action", actions)
               x = actions[0][0]
               y = actions[0][1]
               v = actions[0][2]
               self.board.array[x][y] = v
               self.update()
           print(self.board)

        return True 
            
            
        
    
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
    
    