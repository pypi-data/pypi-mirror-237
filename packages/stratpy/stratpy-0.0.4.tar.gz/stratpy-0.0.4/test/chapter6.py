from stratpy import *

# Creating the game models for Chapter 6

# Figure 6-3
game6_3 = Game(title="Figure 6.3")

# Creating the players
p1, p2 = game6_3.player[1], game6_3.player[2]
p1.name = "South Korea"
p2.name = "Japan"

# Setting up the players utility
a1, a2 = Variable("A_1"), Variable("A_2")
b1, b2 = Variable("B_1"), Variable("B_2")
d1, d2 = Variable("D_1"), Variable("D_2")

# setting the players preferences
b1 > a1 > d1
a2 > b2 > d2

# Adding nodes
(game6_3 + Decision(p1, "Negotiate", variable=(a1, a2))
 + (Decision(p1, "Escalate") + Decision(p2, "Negotiate", variable=(b1, b2)) +
    Decision(p2, "Retaliate", variable=(d1, d2))))

game6_3.export_latex(2.5, "output/6-3.tex")

# Figure 6-4 - with incomplete information
game6_4 = Game(title="Figure 6.4")

nature, p1, p2 = game6_4.player[0], game6_4.player[1], game6_4.player[2]
p1.name = "South Korea"
p2.name = "Japan"

# new payoffs for incomplete game
b2_c = Variable("B_2 - C")

# setting up nature and the resulting information set
info_set = 1
nature_p = Decision(nature, "p", information_set=info_set)
nature_1_p = Decision(nature, "1 - p", information_set=info_set)

# actions for South Korea
sk_a_negotiate = Decision(p1, "Negotiate", variable=(a1, a2))
sk_a_escalate = Decision(p1, "Escalate")
sk_b_negotiate = Decision(p1, "Negotiate", variable=(a1, a2))
sk_b_escalate = Decision(p1, "Escalate")

# actions for Japan
j_a_negotiate = Decision(p2, "Negotiate", variable=(b1, b2_c))
j_a_retaliate = Decision(p2, "Retaliate", variable=(d1, d2))
j_b_negotiate = Decision(p2, "Negotiate", variable=(b1, b2_c))
j_b_retaliate = Decision(p2, "Retaliate", variable=(d1, d2))

# adding nodes to tree structure
game6_4 + nature_p + nature_1_p
# when C is large
nature_p + sk_a_negotiate + sk_a_escalate
sk_a_escalate + j_a_negotiate + j_a_retaliate
# when C is small
nature_1_p + sk_b_negotiate + sk_b_escalate
sk_b_escalate + j_b_negotiate + j_a_retaliate

game6_4.export_latex(2.4, "output/6-4.tex")
