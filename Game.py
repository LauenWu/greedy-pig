import numpy as np
from Player import Player

class Game():
    def __init__(self, player_1:Player, player_2:Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.max_score = 100

    def throw_die(self) -> int:
        return np.random.choice(np.arange(1,7))

    def __is_won(self) -> bool:
        return self.player_1.score >= self.max_score or self.player_2.score >= self.max_score

    def player_play(self, player:Player, other:Player):
        s = 0
        while player.move(player.score, other.score):
            s = self.throw_die()
            if s == 1:
                player.k = 0
                print('k', player.k)
                return
            player.k += s
            print('k', player.k)
        player.score += s

    def play(self):
        won = False

        while not won:
            self.player_play(self.player_1, self.player_2)
            print('player 1:', self.player_1.score)
            if self.__is_won():
                print('player 1 wins')
                won = True
                continue
            self.player_play(self.player_2, self.player_1)
            print('player 2:', self.player_2.score)
            if self.__is_won():
                print('player 2 wins')
                won = True

    
