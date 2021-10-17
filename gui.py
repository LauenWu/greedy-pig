import tkinter as tk
from Game import Game
from Player import Player


class Gui:
    def __init__(self):
        self.game = Game(Player('human'), Player('smart'))

        window = tk.Tk()

        label_p1 = tk.Label(window, text='Player 1')
        label_p1.grid(column=0, row=0, columnspan=2)

        scores_label = tk.Label(
            window, 
            text='{}:{}'.format(self.game.player_1.score, self.game.player_2.score))
        scores_label.grid(column=2, row=0, columnspan=2)

        label_p2 = tk.Label(window, text='Player 2')
        label_p2.grid(column=4, row=0, columnspan=2)

        turn_score_label = tk.Label(window, text='0')
        turn_score_label.grid(column=2, row=1, columnspan=1)

        roll_button = tk.Button(text='roll')
        roll_button.grid(column=0, row=1)

        store_button = tk.Button(text='store')
        store_button.grid(column=1, row=1)

        window.mainloop()

Gui()