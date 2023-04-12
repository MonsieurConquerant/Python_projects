#Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
#Пользователь вводит это число с клавиатуры, список можно считать заданным. 
#Введенное число не обязательно содержится в списке.
elements = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
print('введите число: ')
value = int(input())
def nearest_value(elements, value):
    return min(elements, key=lambda x: abs(value - abs(x)))
print('ближайшее число: ', nearest_value(elements, value))