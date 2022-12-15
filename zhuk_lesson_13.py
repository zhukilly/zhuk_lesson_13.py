#Простейший калькулятор с введением двух чисел типа float.
# Ввод с клавиатуры: операция +-/* (при желании ^√!), два числа
# Каждая операция является функцией
# Обработать деление на ноль
# В качестве завершения программы использовать операцию 0

def add(a, b):
    print(a + b)

def subract(a, b):
    print(a - b)

def multipy(a, b):
    print(a * b)

def divide(a, b):
    print(a / b)

def pow(a, b):
    print(a ** b)
choise = "y"
while choise == "y" or choise == "Y":
    if choise == "0":
        break
    x = float(input("Введите первое число:  "))
    y = float(input("Введите второе число:  "))
    print(".....MENU.......\n 1.Сложение\n 2.Вычитание\n 3.Умножение\n 4.Диление\n 5.Возведение в степень\n ")
    option = int(input("Enter your choice : "))
    if option == 1:
        add(x, y)
    elif option == 2:
        subract(x, y)
    elif option == 3:
        multipy(x, y)
    elif option == 4 and y != 0:
        divide(x, y)
    elif option == 4 and y == 0:
        print('На ноль делить нельзя! ')
        break
    elif option == 5:
        pow(x, y)
    else:
        print("Не верный символ")
    choise = input("Хотите продолжить?-выбирайте-(Y/y), хотите завершить нажмите 0 : ")