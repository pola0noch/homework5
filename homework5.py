#урок "Неизменяемые и изменяемые обЪекты.Кортежи"
immutable_var = 1, "apple",True
print(immutable_var)
#immutable_var[0]=3 невозможно,так как кортеж неизменяем,можно изменить только элементы списка, находящегося в кортеже

mutable_list = [1, 2, "water", False]
mutable_list.append(3)
mutable_list.extend(["cat", 4])
mutable_list.remove("water")
print(mutable_list)