#!/usr/bin/env python3
'''
Functions and classes for representing dice

Niema Moshiri 2020
'''
from random import choice

# named dice
NAMED = {
    'D4':       tuple(range(1,5)),     # 1-4
    'D6':       tuple(range(1,7)),     # 1-6
    'D8':       tuple(range(1,9)),     # 1-8
    'D10_ONES': tuple(range(10)),      # 0-9
    'D10_TENS': tuple(range(0,91,10)), # 0, 10, 20, ..., 90
    'D10_SUM':  tuple(range(100)),     # 0-99
    'D12':      tuple(range(1,13)),    # 1-12
    'D20':      tuple(range(1,21)),    # 1-20
}

# the dice in Dungeons & Dragons
DND = ['D4', 'D6', 'D8', 'D10_ONES', 'D10_TENS', 'D10_SUM', 'D12', 'D20']

class Die:
    '''Class to represent a single die'''
    def __init__(self, sides):
        '''``Die`` constructor

        Args:
            ``sides``: Determine the sides of the die

            * ``list``: The list of sides

            * ``int``: The die will have sides 1, 2, ..., ``sides``

            * ``str``: A standard named die (e.g. "D4", "D6", etc.)
        '''
        if isinstance(sides, str):
            if sides not in NAMED:
                raise ValueError("Invalid die name: %s" % sides)
            self.sides = NAMED[sides]
        elif isinstance(sides, int):
            self.sides = tuple(range(1,sides+1))
        elif isinstance(sides, list) or isinstance(sides, set):
            self.sides = tuple(sides)
        else:
            raise TypeError("'sides' must be 'list' or 'int'")

    def roll(self):
        '''Roll this ``Die``

        Returns:
            ``int``: The value of one of the sides of this ``Die`` with uniform probability
        '''
        return choice(self.sides)

if __name__ == "__main__":
    '''GUI for rolling dice'''
    # relevant imports
    from tkinter import Button,END,Frame,Label,Text,Tk
    from tkinter.font import Font

    # relevant constants
    WINDOW_TITLE = "Dice"
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 400
    HEADER_TEXT = "Dice"
    BG_COLOR = "#002b36"
    BOX_COLOR = "#073642"
    TEXT_BODY_COLOR = "#93a1a1"
    TEXT_HIGHLIGHT_COLOR = "#2aa198"
    TEXT_BAD_COLOR = "#dc322f"
    TEXT_GOOD_COLOR = "#859900"
    BUTTON_PAD_X = 10
    RESULTS_DEFAULT_TEXT = "Select at least one die"

    # initialize main window
    main_window = Tk()
    main_window.title(WINDOW_TITLE)
    main_window.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
    main_window.configure(bg=BG_COLOR)

    # initialize header frame
    header_frame = Frame(master=main_window, bg=BG_COLOR)
    header_frame.pack(side="top", fill="both", expand=True)
    header_label = Label(header_frame, text=HEADER_TEXT, bg=BG_COLOR, fg=TEXT_HIGHLIGHT_COLOR, font=Font(family="Helvetica", size=32, weight="bold"))
    header_label.pack()

    # initialize buttons frame
    buttons_frame = Frame(master=main_window, bg=BG_COLOR)
    buttons_frame.pack(side="top", expand=True)
    die_buttons = dict(); dice = dict()
    for d in DND:
        b = Button(master=buttons_frame, text=d, bg=BG_COLOR, fg=TEXT_BAD_COLOR, padx=BUTTON_PAD_X)
        b.pack(side="left")
        b.config(command=lambda d=d: die_buttons[d].config(fg={TEXT_BAD_COLOR:TEXT_GOOD_COLOR, TEXT_GOOD_COLOR:TEXT_BAD_COLOR}[die_buttons[d].cget('fg')]))
        die_buttons[d] = b; dice[d] = Die(d)

    # initialize roll frame
    roll_frame = Frame(master=main_window, bg=BG_COLOR)
    roll_frame.pack(side="bottom", expand=True)
    def roll_button_func():
        results.delete('1.0',END)
        if sum(die_buttons[d].cget('fg') == TEXT_GOOD_COLOR for d in DND) == 0:
            results.insert(END, RESULTS_DEFAULT_TEXT)
        else:
            for d in DND:
                if die_buttons[d].cget('fg') == TEXT_GOOD_COLOR:
                    results.insert(END, "%s: %s\n" % (d, dice[d].roll()))
    roll_button = Button(master=roll_frame, text="Roll", command=roll_button_func)
    roll_button.pack()

    # initialize results frame
    results_frame = Frame(master=main_window, bg=BG_COLOR)
    results_frame.pack(fill="both", expand=True)
    results = Text(master=results_frame, bg=BOX_COLOR, fg=TEXT_BODY_COLOR, font=Font(family='Courier', size=16))
    results.pack(fill="both", expand=True)
    results.insert(END, RESULTS_DEFAULT_TEXT)

    # run main loop to make window display
    main_window.mainloop()
