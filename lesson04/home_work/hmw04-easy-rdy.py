#1

my_lst = [1, 2, 5]

res_lst = [num ** 2 for num in my_lst]



print(res_lst)


#2

fruits = ['apple', 'orange']

more_fruits = [ 'apple', 'orange', 'pineapple']



both_fruits = [ word for word in fruits if word in more_fruits ]



print(both_fruits)

#3

my_lst = [3, 4]



res_lst = [ num for num in my_lst if (num >= 0) & (num % 3 == 0) & (num % 4 != 0) ]



print(res_lst)
