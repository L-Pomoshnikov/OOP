from random import randint as rnd

class warrior:
    hp = 100

    def setname(self):
        self.name = input()

    def attacking(self):
        print(self.name,'attacking')

    def attacked(self):
        self.hp = self.hp - 20
        print(self.name,'have',(self.hp),'hp')

user1 = warrior()
user2 = warrior()

users = [user1, user2]

user1.setname()
user2.setname()

while (user1.hp > 0) and (user2.hp > 0):
    i = rnd(0,1)
    if i == 0:
        j = 1
    else:
        j = 0
    users[i].attacking()
    users[j].attacked()
    print('----------------')

else:
    print('the end')