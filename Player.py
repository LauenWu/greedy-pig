import numpy as np

class Player:
    def __init__(self, policy:str):
        self.reset()

        if policy == 'human':
            self.policy = policy
        else:
            with open('data/{}_policy.npy'.format(policy), 'rb') as f:
                self.policy = np.load(f)

    def reset(self):
        self.k = 0
        self.score = 0

    def move(self, i,j) -> bool:
        if self.policy == 'human':
            m = bool(int(input('roll?')))
        else:
            m = self.policy[i, j, min(99, self.k)]
        if not m:
            self.score += self.k
            self.k = 0
        return m