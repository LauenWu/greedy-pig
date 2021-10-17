import numpy as np

class Player:
    def __init__(self):
        self.reset()            

    def reset(self):
        self.k = 0
        self.score = 0

    def move(self, roll:bool) -> bool:
        if not roll:
            self.score += self.k
            self.k = 0
        return roll

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)


class ComputerPlayer(Player):
    def __init__(self, policy:str):
        Player.__init__(self)
        with open('data/{}_policy.npy'.format(policy), 'rb') as f:
            self.policy = np.load(f)

    def move(self, other_score:int) -> bool:
        roll = self.policy[self.score, other_score, min(99, self.k)]
        Player.move(self, roll)
        return roll

