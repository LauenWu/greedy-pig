import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PigStrategy:
    def __init__(self, max_score=100):
        self.max_score = max_score
        self.V = np.zeros((max_score, max_score, max_score))
        self.policy = np.zeros((max_score, max_score, max_score)).astype(bool)

    def reward(self, s):
        i,_,k = s
        if i+k >= self.max_score:
            return 1
        return self.V[s]

    def next_states(self, s):
        i,j,k = s
        return [(i,j,k+r) for r in [2,3,4,5,6]]

    def load_V(self):
        with open('data/V.npy', 'rb') as f:
            self.V = np.load(f)

    def load_policy(self):
        with open('data/policy.npy', 'rb') as f:
            self.policy = np.load(f)

    def calculate_V(self, eta=0.00001, gamma=1):
        p = 1/6
        # maximum value improvement
        delta=1
        while delta > eta:
            print(delta)
            delta=0
            for i in self.max_score-1-np.arange(self.max_score):
                for j in self.max_score-1-np.arange(self.max_score):
                    for k in self.max_score-1-np.arange(self.max_score)-i:
                        s = (i,j,k)

                        v = self.V[s]
                        
                        p_hold = 1-self.V[j,i+k,0]
                        p_roll = p*(1 - self.V[j,i,0] + sum([self.reward(s_) for s_ in self.next_states(s)]))
                        
                        self.V[s] = max(p_roll, p_hold)
                        delta = max(delta, np.abs(v-self.V[i,j,k]))

        with open('data/V.npy', 'wb') as f:
            np.save(f, self.V)

    def create_policy(self, plot=False):
        self.load_V()

        max_score=self.V.shape[0]
        p=1/6

        for i in np.arange(max_score):
            for j in np.arange(max_score):
                for k in np.arange(max_score-i):
                    s = (i,j,k)

                    p_hold = 1-V[j,i+k,0]
                    p_roll = p*(1 - V[j,i,0] + sum([self.reward(s_) for s_ in self.next_states(s)]))
                    self.policy[s] = p_roll > p_hold

        with open('data/policy.npy', 'wb') as f:
            np.save(f, self.policy)

        if plot:
            ax = plt.figure(figsize=(10,10)).add_subplot(projection='3d')
            _ = ax.voxels(self.policy)
            ax.set_xlabel('my points')
            ax.set_ylabel('your points')
            ax.set_zlabel('my turn points')
            plt.show()

            #def AnimationFunction(frame):
            #    ax.view_init(30, frame)
            #    plt.draw()

#smart player won  56679 of 100000 games
#0.56679


