from Game import Game
from Player import Player
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#g = Game(Player('human'), Player('smart'))

#g.play()

with open('data/smart_policy.npy', 'rb') as f:
    policy = np.load(f)

def make_animation(policy, f, cumulative=False):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    print(ax)
    _ = ax.voxels(policy)
    ax.set_xlabel('my points')
    ax.set_ylabel('your points')
    ax.set_zlabel('my turn points')

    frames = 360

    def tick(i): 
        ax.view_init(30, i)

    ani = animation.FuncAnimation(fig, tick, frames=frames, interval=50)
    
    writergif = animation.PillowWriter(fps=3) 
    ani.save(f, writer=writergif)
    
make_animation(policy, 'pig.gif')


    