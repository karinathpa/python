
from tkinter import * 
import settings
import utilities
from cell import Cell

root = Tk()
#overriding the settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Mr.clan game')
root.resizable(False, False)


top_frame = Frame(
    root,
    bg='black', #change later to black
    width=settings.WIDTH,
    height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Swiper no swiping!',
    font=('', 48)
)
game_title.place(
    x=utilities.width_prct(25), y=0
)
left_frame= Frame(
    root,
    bg='black', #change later to black
    width=utilities.width_prct(25),
    height=utilities.height_prct(75)
)
left_frame.place(x=0, y=utilities.height_prct(25)) 


center_frame = Frame(
    root,
    bg='black', #change later to black
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)
center_frame.place(
    x=utilities.width_prct(25),
    y=utilities.height_prct(25),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#calling the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()



#run the window
root.mainloop()
