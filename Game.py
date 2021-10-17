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

    def player_turn(self, player:Player, other:Player, output:bool=False):
        s = 0
        while player.move(player.score, other.score):
            s = self.throw_die()
            if s == 1:
                player.k = 0
                if output:
                    print('k', player.k)
                return
            player.k += s
            if output:
                print('k', player.k)
        player.score += s

    def play(self, output:bool=False) -> bool:
        """
        Start a single game

        Returns
        -------
        winning_player : bool
            True -> player 1 wins
            False -> player 2 wins 
        """
        self.player_1.reset()
        self.player_2.reset()

        while True:
            self.player_turn(self.player_1, self.player_2, output)

            if output:
                print('player 1:', self.player_1.score)

            if self.__is_won():
                if output:
                    print('player 1 wins')
                return True

            self.player_turn(self.player_2, self.player_1, output)

            if output:
                print('player 2:', self.player_2.score)

            if self.__is_won():
                if output:
                    print('player 2 wins')
                return False

    
