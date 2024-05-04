import math

def square(side):
    side = float(side)
    area = side * side
    area = math.ceil(area)
    return area

side = input("Введите длину стороны квадрата: ")

print("Площадь квадрата:", square(side))