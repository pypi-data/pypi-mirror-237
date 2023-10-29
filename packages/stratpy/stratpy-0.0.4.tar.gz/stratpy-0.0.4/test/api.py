from stratpy import *

game = Game("Prisoner's Dilemma", player_num=2)
p1 = game.player[1]
p2 = game.player[2]

p1.name = "Japan"
p2.name = "South Korea"

# create utility:
a = Variable("A")
b = Variable("B")
c = Variable("C")
a > b == c

info_set = 1

dec1 = Decision(p1, "Commit", information_set=info_set)
dec2 = Decision(p1, "Do Nothing", information_set=info_set)
dec3 = Decision(p2, "Commit")
dec4 = Decision(p2, "Do nothing", variable=(a, b))
dec5 = Decision(p2, "Retaliate", utility=(1, 1))
dec6 = Decision(p2, "Cooperate", utility=(-1, 100))
dec7 = Decision(p1, "Run away", utility=(4, 2))

(game
 + (dec1 + dec5 + dec6))

dec2.add_nodes(dec3, dec4)

game + dec2

dec3 + dec7 + Decision(p1, "Stay", utility=(7, 9))


game.export_latex(2.5, "output/fig1.tex")


'''
print(game.players)
print(game.title)
print(game.gametype)

print(f"{a.name} : {a.id}")
print(f"{b.name} : {b.id}")
print(f"{c.name} : {c.id}")
print("testing::")



print(b.lower)
print(b.equal)
print(b.higher)

'''
# overload < > == to arrange variables

# a > b == c > d

# create a list with values over and values less

