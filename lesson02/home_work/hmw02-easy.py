
'''# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
'''

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
while i < len(fruits):
    print('{:<}.{:>30}'.format(i+1, fruits[i]))
    i += 1

	
	

'''Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.'''

list1 = [1, "k", "m", 4, 5, 6, 8, 9, 0]
list2 = ["m", 6, 8, 9]


i = 0
j = 0
print(f"Lenght of list1 is:  {len(list1)}")
print(f"Lenght of list2 is:  {len(list2)}")      
while i < len(list1):
    
    while j < len(list2):
        if list1[i] == list2[j]:
            print(f"Element {list1[i]} will be deleted!")
            list1.pop(i)
            i -= 1
            break
        else:
            j += 1
            
           
    i += 1
    j = 0


print(list1)


list1 = [0, 25, 1, 2, 0, 3, 4, 5, 6, 7]
resList = []

for num in list1:
    if num == 0:
        resList.append(num)   
    elif (num % 2) != 0:
        resList.append(num * 2)
    elif (num % 2) == 0:
        resList.append(num / 4)
    else:
        break

print(f"New list looks like that: {resList}")