#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
#  Позиции вводятся с клавиатуры.
import random

n = int(input('Введите число N: ' ))
lst = []

for i in range(n):
     lst.append(random.randint(-n, n))
print(lst) 
ind1 = int(input('Введите позицию первого элемента: '))
ind2 = int(input('Введите позицию второго элемента: '))
proiz = lst[ind1] * lst[ind2]
print(proiz)
