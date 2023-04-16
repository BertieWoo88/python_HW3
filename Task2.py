'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

from random import randint
n = int(input("введите размерность массива: "))
listA = []
for i in range(n):
    listA.append(randint(0,9))
print(*listA)
#listA.sort() 
#print(listA)  
x = int(input("введите число: "))
raz = abs(listA[0]-x)
answ = listA[0] 
for i in listA:
    if abs(x-i)<=raz and i!=x:
        #print(raz)
        raz = abs(x-i)
        answ = i
print(answ)
