from stratpy import *

# Creating the game models for Chapter 5

# Model 1a
game5_1a = Game(title="Model 1a", player_num=2)

# Creating the players
p1, p2 = game5_1a.player[1], game5_1a.player[2]
p1.name = "South Korea"
p2.name = "Japan"

# Setting up the players utility
s1, s2 = Variable("S_1"), Variable("S_2")
d1, d2 = Variable("D_1"), Variable("D_2")
s1_g, s2_a = Variable("S_1 + G"), Variable("S_2 - A")

# setting the players preferences
s1_g > s1 > d1
s2 > s2_a > d2

# Adding nodes
(game5_1a + Decision(p1, "Refrain", variable=(s1, s2))
          + (Decision(p1, "Persist") + Decision(p2, "Punish", variable=(d1, d2)) +
                                       Decision(p2, "Ignore", variable=(s1_g, s2_a))))

game5_1a.export_latex(1.5, "output/5-1a.tex")

# Model 1b
game5_1b = Game(title="Model 1b", player_num=2)

# Creating the players
p1, p2 = game5_1b.player[1], game5_1b.player[2]
p1.name = "South Korea"
p2.name = "Japan"

# Adding nodes to the tree
(game5_1b + Decision(p1, "Refrain", utility=(3, 3))
 + (Decision(p1, "Persist") + Decision(p2, "Punish", utility=(1, 1)) +
    Decision(p2, "Ignore", utility=(4, 2))))

game5_1b.export_latex(1.5, "output/5-1b.tex")

# Model for 5-2 - with incomplete information

game5_2 = Game("Incomplete Information")
nature, p1, p2 =game5_2.player[0], game5_2.player[1], game5_2.player[2]
p1.name = "South Korea"
p2.name = "Japan"

# new information set
info_set = 1

# actions for nature
# the probabalistic action causes the information set 1
nature_p = Decision(nature, "p", information_set=info_set)
nature_1_p = Decision(nature, "1 - p", information_set=info_set)

# actions for South Korea
a_refrain = Decision(p1, "Refrain", variable=(s1, s2))
a_persist = Decision(p1, "Refrain")
b_refrain = Decision(p1, "Refrain", variable=(s1, s2))
b_persist = Decision(p1, "Refrain")

# actions for Japan
a_punish = Decision(p2, "Punish", variable=(d1, d2))
b_punish = Decision(p2, "Punish", variable=(d1, d2))
b_ignore = Decision(p2, "Ignore", variable=(s1_g, s2_a))

# adding nodes to tree structure
game5_2 + nature_p + nature_1_p
# A side
nature_p + a_refrain + a_persist
a_persist + a_punish
# B side
nature_1_p + b_refrain + b_persist
b_persist + b_punish + b_ignore

# Export the game as latex
game5_2.export_latex(2.5, "output/5-2.tex")
