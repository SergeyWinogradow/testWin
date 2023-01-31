import random

Robot1 = 100
Robot2 = 100

while 1:
    print("Бой роботов начался")
    a = input("Бой!")
    number1 = random.randint(0, 50)
    print("Атака робота 1 ", number1)
    number2 = random.randint(0, 50)
    print("Атака робота 2 ", number2)
    if number1 > number2:
        Udar1 = number1 - number2
        Robot2 = Robot2 - Udar1
        print("Robot1 нанес Robot2 ", Udar1, "Прочности осталось ", Robot2)
        if Robot2 <= 0:
                print("в бою победил Robot1 с", Robot1, "прочности")
                print()
                break
    elif number1 < number2:
        Udar2 = number2 - number1
        Robot1 = Robot1 - Udar2
        print("Robot2 нанес Robot1 ", Udar2, "Прочности осталось ", Robot1)
        if Robot1 <= 0:
            print("в бою победил Robot2 с", Robot2, "прочности")
            print()
            break
    else:
        print("Противники обменялись ударами")



