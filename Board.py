import numpy as np

class Board:
    def __init__ (self, array, dim, empty_cells, rows, cols):
        self.array = array
        self.dim = dim
        self.empty_cells = empty_cells #Number of empty cells
        self.row_tally = rows # A list of lists to store the tally of 0's and 1's for each row. 
        self.col_tally = cols # A list of lists to store the tally of 0's and 1's for each column.
        
    def __repr__(self):
        res = ""
        for i in range(self.dim):
            for j in range(self.dim):
                res += str(self.array[i][j])
                if j < self.dim - 1:
                    res += "\t"
            if i < self.dim - 1:
                res += "\n"
        return res
    
    def get_row(self, row: int) -> tuple:
        return tuple(self.array[row][: self.dim])

    def get_column(self, col: int) -> tuple:
        return tuple(row[col] for row in self.array[:self.dim])
    
    def get_number(self, row: int, col: int) -> int:
        return self.array[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int) -> tuple:
        v1 = self.array[row + 1][col] if (row < self.dim - 1) else (None)
        v2 = self.array[row - 1][col] if (row > 0) else (None)
        return (v1, v2)
    
    def adjacent_horizontal_numbers(self, row: int, col: int) -> tuple:
        v1 = self.array[row][col - 1] if (col > 0) else (None)
        v2 = self.array[row][col + 1] if (col < self.dim - 1) else (None)
        return (v1, v2)
    
    def two_numbers(self, row: int, col: int, mode) -> tuple:
        if mode == "below":
            v1 = self.array[row + 2][col] if (row < self.dim - 2) else (None)
            v2 = self.array[row + 1][col] if (row < self.dim - 1) else (None)
        elif mode == "above":
            v1 = self.array[row - 1][col] if (row > 0) else (None)
            v2 = self.array[row - 2][col] if (row > 1) else (None)
        elif mode == "previous":
            v1 = self.array[row][col - 2] if (col > 1) else (None)
            v2 = self.array[row][col - 1] if (col > 0) else (None)
        elif mode == "following":
            v1 = self.array[row][col + 1] if (col < self.dim - 1) else (None)
            v2 = self.array[row][col + 2] if (col < self.dim - 2) else (None)
        return (v1, v2)
    
    @staticmethod
    def parse_instance_from_stdin():
        mat = []
        dim = int(input())
        for f in range(dim):
            mat.append([int(i) for i in input().split()])
        empty_cells = 0
        row_tally = []
        col_tally = []
        for i in range(dim):
            row_tally.append([0, 0])
            col_tally.append([0, 0])
        for i in range(dim):
            for j in range(dim):
                val = mat[i][j]
                if val != 2:
                    empty_cells += 1
                    row_tally[i][val] += 1
                    col_tally[j][val] += 1
        return Board(np.array(mat), dim, empty_cells, row_tally, col_tally)
    
    def apply_action(self, action):
        array = np.copy(self.array)
        array[action[0]][action[1]] = action[2]
        new_empty_cells = self.empty_cells - 1
        new_row_tally = []
        new_col_tally = []
        for i in range(self.dim):
            new_row_tally.append(self.row_tally[i].copy())
            new_col_tally.append(self.col_tally[i].copy())
        new_row_tally[action[0]][action[2]] += 1
        new_col_tally[action[1]][action[2]] += 1
        return Board(array, self.dim, new_empty_cells, new_row_tally, new_col_tally)



