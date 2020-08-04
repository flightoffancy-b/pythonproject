#Квадратное уравнение, где ни один коэфицентов не  равен нулю 
import math

print('Введите коэфиценты уравнения ax^2  + bx + c = 0 больше нуля')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

Discr = b ** 2 - 4 * a * c

if Discr <  0:
    print('Корней нет, приятель')
else: 
    if Discr > 0:
        x1 = (-b + math.sqrt(Discr)) / (2 * a)
        x2 = (-b - math.sqrt(Discr)) / (2 * a)
        print("x1 = "+str(x1))
        print("x2 = "+str(x2))
    else: 
        x1 = -b / (2 * a)
        print("x1 = "+str(x1))
            