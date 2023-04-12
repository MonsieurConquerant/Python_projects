# Напишите рекурсивную функцию sum(a, b), возвращающую 
# сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Циклы использовать нельзя

print('введите а: ')
a = int(input())
print('введите b: ')
b = int(input())

def recursion(a, b):
    if b == 0:
        return a
    else:
        return recursion(a, b)
 
print(recursion(a, b))
