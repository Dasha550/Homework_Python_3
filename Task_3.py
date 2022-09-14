#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


numbers=[1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(numbers)):
    numbers[i]=(round((numbers[i]- int (numbers[i])),2))
unnecessary_index = numbers.index(0)
numbers.pop(unnecessary_index)
        
max_floor = max(numbers)
min_floor = min(numbers)
print(max_floor-min_floor)