# Задача N25. Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

input_str = 'a a a b c a a d c d d'
input_list = input_str.split()
# input_str = 'a/a/a/b/c/a/a/d/c/d/d' если бы было так, то
# input_list = input_str.split(/) 
print(input_list)
res = []

for i in range(len(input_list)):
    x = input_list[:i]
    if x.count(input_list[i]) == 0:
        res.append(input_list[i])
    else:
        res.append(f'{input_list[i]}_{x.count(input_list[i])}')
print(res)
out_str = ' '.join(res)
print(out_str)
