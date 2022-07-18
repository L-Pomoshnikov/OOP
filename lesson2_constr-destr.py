class Person:
    def __init__(self, n:str, l:str, q:int = 1 ):
        self.name = n
        self.lastname = l
        self.qualif = q

    def info(self):
        print(self.name, self.lastname, self.qualif)

    def __del__(self):
        print('До свидания, мистер', self.name, self.lastname, sep = " ")

emp1 = Person('Alex', 'Ivanov', 3)
emp2 = Person('John', 'Night')
emp3 = Person('James', 'Jordan', 2)

employees = [emp1, emp2, emp3]

for emp in employees:
    emp.info()

out = employees[0]
for emp in employees[1:]:
    if emp.qualif < out.qualif:
        out = emp

out.__del__()
print('------------------------------------')
input()