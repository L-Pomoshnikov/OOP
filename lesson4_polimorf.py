class a:
    def __init__(self, i): 
        self.id = i 

    def __str__(self): #перегрузка метода print
        return str(self.id) #нужно создать какую-либо строку

class b:
    def __init__(self, i): 
        self.id = i
    
    def __add__(self, other): #перегрузка оператора +
        x3 = b(3) #по условию задачи создаётся новый объект такого же класса
        return x3 

x1 = a(1)
x2 = b(2)

print(x1)
print(x2 + x1)