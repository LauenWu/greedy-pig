# greedy-pig

This article was inspired by the paper [Optimal Play of the Dice Game Pig -Todd W. Neller, Clifton G.M. Presser](https://cupola.gettysburg.edu/cgi/viewcontent.cgi?article=1003&context=csfac, "paper").

Greedy Pig is a dice game for 2 or more players. The rules are fairly simple: each turn a player repeatedly throws a die. After each throw he has the choice of stopping and storing his thrown score in his bank or to continue until he throws a 1. Then, his turn will be over and his unstored score is lost. The winner is whoever reaches a score of at least 100 points first.

So you can go for a greedy strategy and risk on loosing an increasing amount of points, or you go for a save strategy and store even small amounts of points. The strategy may also depend on my own points and the points of my opponent. For example, if I have 20 points and my opponent is already at 80, I might have to go for a risky play to catch up before the game is over.

The cool thing about Greedy Pig is, that each game state can be completely described by three numbers:
* my banked points (save)
* my turn points (not save)
* the opponents' points
Imagine a cube where each dimension represents one of the numbers above. For each coordinate in that cube, we could decide whether we roll again or store our score. The result would be a cube consisting of booleans (True or False) which perfectly describes a player's strategy. This cube can be visualized and for a random strategy could look something like this:
![](https://github.com/ML-pool/greedy-pig/blob/main/data/random_policy.png)

At states where I'm inside a blue body, I play on, where there is no blue, I store my points. Notice how the upper triangle is missing. This is due to the fact that a player having, let's say, 80 points in the bank and 20 turn points, he wins automatically.

There is an optimal way of playing Greedy Pig. It is not that simple to find, since you have to solve a system of 505'000 linear equations. Since that is for sure not a pen & paper task, I used `value iteration` (as recommended by Neller & Presser) to find the probability of winning in each state (see my implementation on GitHub). The optimal strategy (roll or store) derived from those probabilities then looks as follows:
![](https://github.com/ML-pool/greedy-pig/blob/main/data/smart_policy.gif)

It seems amazing that such a simple game can have an optimal strategy that complicated. I wonder what that may look like for a more complicated game like Monopoly...
