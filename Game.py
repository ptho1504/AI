
import settings
import utils
from tkinter import *
from tkinter import messagebox
import time


    
def onClickfinish(event, boardcopy):
    def finish(boardcopy):
        # print(boardcopy)
        if(goal_test(boardcopy)):
            messagebox.showinfo("Finish", "Good job")
        else:
            messagebox.showinfo("Failed", "Try again")
    finish(boardcopy)

def onClickAuto(event, solved):
    def auto(solved):
        # print(solved)
        if Game.step < len(solved):
            s = solved[Game.step]
            x = s[0]
            y = s[1]
            value = s[2]
            Game.step += 1
            Cell.changeState(x,y,value)
            Game.cell_dict[(x,y)].cell_btn_object['text'] = value
            
        # print(Game.boardcopy)
    auto(solved)
    

def onClickReset(event, ): pass
    


def update(board):
        empty_cells = 0
        row_tally = []
        col_tally = []
        dim = board.dim
        for i in range(dim):
            row_tally.append([0, 0])
            col_tally.append([0, 0])
            
        for i in range(dim):
            for j in range(dim):
                val = board.array[i][j]
                if val != 2:
                    empty_cells += 1
                    row_tally[i][val] += 1
                    col_tally[j][val] += 1
        
        board.row_tally = row_tally
        board.col_tally = col_tally
        board.empty_cells = dim*dim - empty_cells

def goal_test(board):
    row_t = board.row_tally
    col_t = board.col_tally
    dim = board.dim
    
    #Check sum of number 0s and number 1s in one row == dim
    for i in range(dim):
        if sum(row_t[i]) != dim:
            # print("123")
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

class Cell:
    def __init__(self,x,y, value):
        self.value = value
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # self.values = [0,1,2]
    
    def create_btn_object(self, location, value):
        
        btn_text = f"{value}" if value in [0,1] else "-"
        
        btn = Button(
            location, 
            width=4,
            height=2,
            text = btn_text,
            font=('consolas', 8, 'bold'),
            foreground ="red"
        )
        # print("value", value, btn_text)
        # print(self.x, self.y, self.value, btn_text)
        if value != 2:
            btn.config(state='disabled', bg='#a0aec0')
        else:
            btn.config(state='disabled', bg='#4299e1' )
            btn.bind('<Button-1>',  self.left_click_actions) # Left Click
        
        self.cell_btn_object = btn

    @staticmethod
    def changeState(x,y,value):
        Game.boardcopy.array[x][y] = value
        update(Game.boardcopy)
        
        # print(Game.boardcopy)
        # print("")
        
    
    def left_click_actions(self, event):
        # print(event)
        if self.value == 2:
            self.value = 0
            self.cell_btn_object['text'] = self.value
        elif self.value == 1:
            self.value = 2
            self.cell_btn_object['text'] = ""
        else :
            self.value = 1
            self.cell_btn_object['text'] = self.value
        
        self.changeState(self.x, self.y, self.value)
        # print(self.x, self.y, self.value)
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
    
        
    


class Game:
    boardcopy = []
    def __init__(self, boardcopy, dim,solved) :
        Game.boardcopy = boardcopy
        self.solved = solved
        Game.step = 0
        Game.cell_dict = {}
        root = Tk()
        
        # Override the setting of the window
        root.config(bg="black")
        root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
        root.title("Binary Puzzle")
        # root.resizable(False,False)

        top_frame = Frame(
            root,
            bg='black',
            width=settings.WIDTH,
            height=utils.height_prct(10)
        )

        top_frame.place(x = 0, y = 0)

        left_frame = Frame(
            root,
            bg='black',
            width=utils.width_prct(10),
            height= utils.height_prct(65)
        )
        left_frame.place(x=0,y=utils.height_prct(25))

        center_frame = Frame(
            root,
            bg='black',
            width=utils.width_prct(85),
            height=utils.height_prct(85)
        )

        center_frame.place(x=utils.width_prct(30),y=utils.height_prct(5))

        finish_button = Button(text = "Finish", bg="red", font=('consolas', 20),width=10)
        finish_button.bind('<Button-1>', lambda event :  onClickfinish(Event,boardcopy))
        
        finish_button.grid(
            column= 20,
            row= 0,
            sticky=NE
        )

        auto_button = Button(text = "Next", bg="red", font=('consolas', 20), width=10)
        auto_button.bind('<Button-1>', lambda event :  onClickAuto(Event, self.solved))
        auto_button.grid(
            column= 20,
            row= 60
        )
        
        
        
        
        for x in range(dim):
            for y in range (dim):
                value = Game.boardcopy.array[x][y]
                c = Cell(x,y,value)
                c.create_btn_object(center_frame,value)
                c.cell_btn_object.grid(
                    column= y,
                    row = x
                )
                self.cell_dict[(x, y)] = c
                # print(c)
        
        #Run the window
        root.mainloop()
    