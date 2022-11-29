#Реализуйте алгоритм перемешивания списка.
import random


def mix_list(list_first):
    list = list_first[:]
    lst_length = len(list)
    for i in range(lst_length):
        index_rand = random.randint(0, lst_length - 1)
    #меняем индекс
        temp = list[i]
        list[i] = list[index_rand]
        list[index_rand] = temp 
    return list


list = [1,2,3,4,5,6]
mixed_list = mix_list(list)
print(list)
print(mixed_list)
