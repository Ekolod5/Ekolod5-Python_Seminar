# Задача N47. У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине 
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно 
# получить его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) 
# if values == transformed_values:
#     print(‘ok’) 
#       else:
#     print(‘fail’)
# Вывод:
# ok


def f(x):
    return x   # для проверки работает ли return x*2


def f2(x, y):
    list_1 = []
    for i in y:
        list_1.append(x(i))
    return list_1


values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transformed_values = list(map(f, values))


print(values)
print(transformed_values)
    