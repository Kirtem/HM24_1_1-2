# Задание 1 к 1 уроку
square_length = int(input("Введите длину стороны квадрата: "))
# print("Периметр квадрата: ", p)
# print("Площадь квадрата: ", s)
rectangle_length = float(input("Введите длину прямоугольника: "))
rectangle_area = float(input("Введите ширину прямоугольника: "))
simvol = input("Введите разделитель: ")
square_per = int(square_length * 4)
print("Площадь квадрата: ", square_length ** 2)
rectangle_pl = int(rectangle_area * rectangle_length)
print(simvol * (square_per + rectangle_pl))
print("Периметр прямоугольника: ", 2 * (rectangle_length + rectangle_area))
# rectangle_pl = print("Площадь прямоугольника: ", rectangle_area * rectangle_length)
print("Площадь прямоугольника: ", rectangle_area * rectangle_length)
saler = int(input("Введите заработную плату в месяц: "))
proc_ipoteka = int(input("Введите, какой процент(%) уходит на ипотеку: "))
proc_live = int(input("Введите, какой процент(%) уходит на жизнь: "))


print("На ипотеку было потрачено: ", saler/100 * proc_ipoteka, "рублей")
print("Было накоплено: ", saler - saler/100 * (100 - proc_ipoteka - proc_live), "рублей")


