from random import randint as rnd

class unit:
    def __init__(self, a, b):
        self.id = a
        self.team = b
    
class soldier(unit):
    def follow_hero(self, a:unit):
        print('soldier ' + str(self.id) + ' follows hero ' + str(a.id))

class hero(unit):
    def lvl_up(self):
        print('hero ' + str(self.id) + ' ups his level')

team1, team2 = [], []
teams = [team1, team2]

team1.append(hero(1, team1))
team2.append(hero(2, team2))

for i in range(9):
    t = rnd(0, 1)

    s = soldier(i + 3, t)
    teams[t].append(s)

l1, l2 = len(team1), len(team2)
print('team1 -',l1,';','team2 -',l2)

if l1 > l2:
    x = team1
else:
    x = team2

x[0].lvl_up()
x[1].follow_hero(x[0])