#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

numbersStart=[2, 3, 5, 6]
numbersGap=numbersStart[int(((len(numbersStart))/2))::]
numbersEnd= numbersGap[::-1]
product_of_numbers=[]
for i in range(len(numbersEnd)):
    product_of_num=numbersStart[i]*numbersEnd[i]
    product_of_numbers.append(product_of_num)
print(product_of_numbers)