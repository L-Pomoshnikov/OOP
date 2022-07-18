class pharmacy:
    def __init__(self, b, l): 
        self.brand = b
        self.location = l
    
    __margin = 0 #скрытое поле

    def setMargin(self): #сеттер - устанавливаем значение скрытого поля с помощью метода
        x = int(input())
        self.__margin = x
    
    def getMargin(self): #геттер - получаем значение скрытого поля с помощью метода
        password = int(input('input password - ')) #для получения необходимо ввести пароль:)
        if password == 1111:
            print('margin is ',self.__margin)
        else:
            print('you have no rights')


Bauman = pharmacy('GZ', 'street')

print(Bauman.brand, Bauman.location)
Bauman.setMargin()
Bauman.getMargin()


