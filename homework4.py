immutable_var = (1, 2, "hard", True)
print(type(immutable_var))
print(immutable_var)
# immutable_var[0] = 12 - кортеж не поддерживает обращение по элементам
immutable_var_1 = ([5, 8], "hard", "tuple")
print(immutable_var_1)
immutable_var_1[0][0] = 9
print(immutable_var_1)
immutable_var_1[0][1] = 13
print(immutable_var_1)
mutable_list = [1, 2, "hard", True]
print(type(mutable_list))
print(mutable_list)
mutable_list[2] = "easy"
mutable_list.remove(int("1"))
mutable_list.append("Modified")
print(mutable_list)
