# Задача N3. В некоторой школе решили набрать три новых математических 
# класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) 
# Output: 32

klass_a = int(input('Введите количество учеников: '))
klass_b = int(input('Введите количество учеников: '))
klass_c = int(input('Введите количество учеников: '))

res = round((klass_a + klass_b + klass_c) / 2)
print(res)
