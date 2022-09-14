#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10


numbers_decimal = 45
 
numbers_binary = ''
 
while numbers_decimal > 0:
    numbers_binary = str(numbers_decimal % 2) + numbers_binary
    numbers_decimal = numbers_decimal // 2
print(numbers_binary)