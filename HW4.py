#Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
import random

'''arr = [1, 5, 2, 3, 4, 6, 1, 7]
array = [arr[0]]
min = arr[0]
for j in range(len(arr)):
    if min < arr[j]:
        array.append(arr[j])
        min = arr[j]
    elif array[len(array)-1] > arr[j] > array[len(array)-2]:
        array.remove(min)
        array.append(arr[j])
        continue
print(array)'''

#Cоздать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 
'''
with open('file.txt', 'w') as nums:
    length = random.randint(3, 20)
    for i in range(length):
        nums.write(f'{random.randint(0, 101)}' + ' ')
    nums.write('\n')

with open('file.txt', 'r+') as nums:
    arr1 = nums.readline()
    arr = []
    s = ''
    for m in range(len(arr1)):
        if arr1[m] != ' ':
            s += arr1[m]
        else:
            arr.append(int(s))
            s = ''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                max = arr[i]
                arr[i] = arr[j] 
                arr[j] = max
                continue
    for i in arr:
        nums.write(f'{i}' + " ")
'''
#Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
#Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7] [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#Порядок элементов менять нельзя

'''arr = [1, 5, 2, 3, 4, 6, 1, 7]
min = arr[0]
for j in range(len(arr)):
    if arr[j] <= min:
        min = arr[j]
        c = j
array = [arr[c]]
for i in range(len(arr)):
    if arr[i] > array[len(array)-1]:
        array.append(arr[i])
    elif array[len(array)-2] < arr[i] < array[len(array)-1]:
        array.remove(array[len(array)-1])
        array.append(arr[i])
print(array)'''