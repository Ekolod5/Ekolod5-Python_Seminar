"""Задача N31. Последовательностью Фибоначчи называется последовательность 
чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
Требуется найти N-е число Фибоначчи.
Input: 7 
Output: 8
Задание необходимо решать через рекурсию"""

def find_fibo(x, fibo_lst=[0, 1]):  # объявляем ф-цию, где число х - номер числа Фиббоначи, которое надо вывести, + список с первыми двумя числами
    if len(fibo_lst) == x:  # если порядковый номер числа равен длине списка ...
        print(fibo_lst)  # ... печатаем для наглядности список...
        return fibo_lst[-1]   # ... и возвращаем последнее число из списка
    else:
        fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])   # добавляем в список новое число
    return find_fibo(x, fibo_lst)   # заходим в рекурсию до тех пор, пока порядковый номер числа не будет равен длине списка

print(find_fibo(int(input('Введите номер числа Фиббоначи: '))))
