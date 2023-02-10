# Задача 11. Дано натуральное число A > 1. Определите, каким по счету 
# числом Фибоначчи оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 
# Output: 6

user_input = int(input('Введите целое положительное число: '))  
fibo_nums = [0, 1]
n = fibo_nums[1]
while n < user_input:
    n = fibo_nums[-1] + fibo_nums[-2]
    fibo_nums.append(n)
if user_input in fibo_nums:
    print(f'{user_input} - число Фиббоначи № {fibo_nums.index(user_input) + 1}')
else:
    print(f'{user_input} - не является числом Фиббоначи')
