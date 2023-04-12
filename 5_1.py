# Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
print('введите а: ')
a = int(input())
print('введите b: ')
b = int(input())

def recursion(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / recursion(a, -b)
    if b % 2 == 0:
        return recursion(a, b // 2) * recursion(a, b // 2)
    else:
        return recursion(a, b - 1) * a
    
print(recursion(a, b))
