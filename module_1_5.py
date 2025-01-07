immutable_var = (1, 2, "a", "b")
print(immutable_var)
immutable_var[0] = 100 # Кортежи являются неизменяемыми структурами данных. После создания кортежа - изменять,
# добавлять или удалять его элементы невозможно. Для изменения лучше использовать списки
mutable_list = [2, 3, 'c', 'd', 'list']
mutable_list [0]= 1
mutable_list [1] = 2
mutable_list [2] = "a"
mutable_list [3] = "b"
mutable_list [4] = 'Modified'
print(mutable_list)