import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import binvox_rw
from binvox_rw import Voxels

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

                    p_hold = 1-self.V[j,i+k,0]
                    p_roll = p*(1 - self.V[j,i,0] + sum([self.reward(s_) for s_ in self.next_states(s)]))
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

def plot_policy(policy):
    """
    Creates a voxel plot of a policy

    ...
    
    Parameters:
    -----------
    policy : str
        name of policy
    """
    with open('data/{}_policy.npy'.format(policy), 'rb') as f:
        policy_data = np.load(f)

    ax = plt.figure(figsize=(10,10)).add_subplot(projection='3d')
    _ = ax.voxels(policy_data)
    ax.set_xlabel('my points')
    ax.set_ylabel('opponents points')
    ax.set_zlabel('my turn points')
    plt.show()

def make_animation(policy):
    """
    Creates and stores a .gif animation of a policy

    ...
    
    Parameters:
    -----------
    policy : str
        name of policy
    """

    with open('data/{}_policy.npy'.format(policy), 'rb') as f:
        policy_data = np.load(f)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    _ = ax.voxels(policy_data)
    ax.set_xlabel('my points')
    ax.set_ylabel('your points')
    ax.set_zlabel('my turn points')

    frames = 360

    def tick(i):
        print(i/frames*100, '%') 
        ax.view_init(30, 360-i)

    ani = animation.FuncAnimation(fig, tick, frames=frames, interval=5)
    
    writergif = animation.PillowWriter(fps=30) 
    ani.save('data/' + policy + '_policy.gif', writer=writergif)

def make_binvox(policy):
    """
    creates and stores a .binvox file of a policy

    ...

    Parameters:
    -----------
    policy : str
        name of policy ('hold20', 'smart')
    """
    with open('data/{}_policy.npy'.format(policy), 'rb') as f:
        policy_data = np.load(f)

    v = Voxels(data=policy_data, dims=(100,100,100), translate=(0,0,0), scale=1, axis_order='xyz')
    with open('data/{}_policy.binvox'.format(policy), 'wb') as f:
        v.write(f)

#smart player won  56679 of 100000 games
#0.56679


