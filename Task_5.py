#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
ambitFib = 8
fibList=[]
fib1 = fib2 = 1
for i in range(-1, ambitFib):
    fib1, fib2 = fib2, fib1 - fib2
    fibList.append(fib2)
fibList.reverse()

fib1 = fib2 = 1
fibList.append(fib1)
fibList.append(fib2)

for i in range(2, ambitFib):
    fib1, fib2 = fib2, fib1 + fib2
    fibList.append(fib2)
print(fibList)
