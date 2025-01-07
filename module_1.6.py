my_dict = {'Vasya': 1975,
           'Egor': 1999,
           'Masha': 2002}
print(my_dict)
print(my_dict["Masha"]) # существующий ключ
print(my_dict.get("Petr")) # отсутсвующий ключ
my_dict["Kamila"] = 1981 # добавление произвольной пары
my_dict["Artem"] = 1915 # добавление произвольной пары
a = my_dict.pop('Egor') # удаление пары
print(a)
print(my_dict)
my_set = {1,"Яблоко",42.314}
print(my_set)
my_set.add((5,6,1.6))
my_set.add(13)
my_set.remove(1)
print(my_set)