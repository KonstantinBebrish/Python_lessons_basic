# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    # Fn = Fn-1 + Fn-2
    
    fibonacciRow = [1, 1]

    for i in range(2, m):
        fibonacciRow.append(fibonacciRow[i - 1] + fibonacciRow[i - 2])

    fibonacciRow = fibonacciRow[n:m]  

    

    return fibonacciRow


print(fibonacci(78,102))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def sortToMax(originList):
    if len(originList) <= 1:
        return originList
    else:
        x = random.choice(originList)
    
    lowerNums = [n for n in originList if n < x]
 
    equalNums = [x] * originList.count(x)
    biggerNums = [n for n in originList if n > x]
  
    return sortToMax(lowerNums) + equalNums + sortToMax(biggerNums)
    

    
print(sortToMax([10, 2, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


num_lst = [1, 2, 3, -1, 0, -2, 4]

def my_filter(greater_zero, num_lst):

    result = [num for num in num_lst if greater_zero() == True]
    
    return result

	
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math

def vertex_traillogram(A1, A2, A3, A4):
    
    len_A1A2 = math.sqrt(( A2[0] - A1[0] ) ** 2 + ( A2[1] - A1[1] ) ** 2 )
    len_A4A3 = math.sqrt(( A3[0] - A4[0] ) ** 2 + ( A3[1] - A4[1] ) ** 2 )
    len_A1A4 = math.sqrt(( A4[0] - A1[0] ) ** 2 + ( A4[1] - A1[1] ) ** 2 )
    len_A2A3 = math.sqrt(( A3[0] - A2[0] ) ** 2 + ( A3[1] - A2[1] ) ** 2 )
    if (len_A1A2 == len_A4A3) & (len_A1A4 == len_A2A3):
          return True
    else:
          return False

print(vertex_traillogram((1, 3), (4, 7), (2, 8), (-1, 4)))



