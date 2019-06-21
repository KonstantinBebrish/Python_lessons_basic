# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.


# w/o re

my_str = "mtMmEZUOmcq"  # result to achieve ['mt', 'm', 'mcq']

all_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                 'x', 'y', 'z', ]
result = []
str_out = ""

for letter in my_str:
    if letter in all_lowercase:
        str_out += letter
    else:
        str_out += " "

result = str_out.split()

print(f"The output is:  {result}")

# with re

result = re.findall(r"[abcdefghijklmnopqrstuvwxyz]+", "mtMmEZUOmcq")

print(f"The output list is: {result}")
