from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y


    #appending the obect of the cell. all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text= f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.surrounded_cells_mines_length ==0:
                for cell__obj in self.surrounded_cells:
                    cell__obj.show_cell()
            self.show_cell()
            #if the mine count and the cell count is equal then displaying win message
            if Cell.cell_count == settings.MINES_COUNT:
                 ctypes.windll.user32.MessageBoxW(0, 'Not so dumb, maybe?', 'Dead Bro!', 0)


        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
        #return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y ==y:
                return cell
    @property
    def surrounded_cells(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1 ),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y +1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        

        cells = [cell for cell in surrounded_cells if cell is not None]
        return cells
    

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
    

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #replacing it with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}")

            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )









    #mark the cell as opened (use it as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        #concept to interrupt the game and display a message that player lost
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'Youre just dumb', 'Dead Bro!', 2)
        sys.exit()
       
        

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate= True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
       
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"