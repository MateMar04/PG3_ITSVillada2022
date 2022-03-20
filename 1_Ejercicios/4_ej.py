from random import randint


list = []

for i in range(50):
    list.append(randint(0, 1000))

sorted_list = sorted(list)

print(sorted_list)
