from random import randint
from typing import List

list: List[int] = []

for i in range(50):
    list.append(randint(0, 1000))

sorted_list: List[int] = sorted(list, reverse=True)

print(sorted_list)
