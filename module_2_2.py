# вывести 3
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first == second and second == third:
    print(3)
# вывести 2
if first == second:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
# вывести 0
else:
    print(0)
