from Game import Game
from Player import Player
import numpy as np
import matplotlib.pyplot as plt
from PigStrategy import make_binvox

g = Game(Player('smart'), Player('hold20'))

# compare players by calculating the odds
victories_p1 = 0
victories_p2 = 0

for i in range(10000):
    v = g.play()
    if v:
        victories_p1 += 1
    else:
        victories_p2 += 1

    if not victories_p2 == 0:
        print('odds p1', victories_p1/victories_p2)

    