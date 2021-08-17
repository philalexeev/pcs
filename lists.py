# creating lists

from typing import Collection


colors = ['red', 'green', 'blue', 'cyan', 'magenta']
type(colors)
# <class 'list'>

list(('red', 'green', 'blue', 23, True))
# ['red', 'green', 'blue', 23, True]

list('Python')
# ['P', 'y', 't', 'h', 'o', 'n']

'Python, JavaScript, Rust'.split(', ')
# ['Python', 'JavaScript', 'Rust']

'Python'.split('c')
# ['Python']


# basic operations

colors[2]
# 'blue'

colors[2:5]
# ['blue', 'cyan', 'magenta']

'green' in colors
# True

for item in colors:
    print(item)


# mutability (using index and slice notation)

colors[1] = 'orange'
# ['red', 'orange', 'blue', 'cyan', 'magenta']

colors[1:3] = ['black', 'brown']
# ['red', 'black', 'brown', 'cyan', 'magenta']

colors[1:4] = ['pink']
# ['red', 'pink', 'magenta']


# methods

colors.insert(1, 'maroon')
# ['red', 'maroon', 'pink', 'magenta']

colors.insert(10, 'black')
# ['red', 'maroon', 'pink', 'magenta', 'black']
# added to the end

colors.insert(-1, 'tomato')
# ['red', 'maroon', 'pink', 'magenta', 'tomato', 'black']
# added to the beforend position

returned_value = colors.pop(2)
# retured_value == 'pink'
# colors == ['red', 'maroon', 'magenta', 'tomato', 'black']
# remove element

returned_value = colors.pop(-1)
returned_value == 'black'
# colors == ['red', 'maroon', 'magenta', 'tomato']

returned_value = colors.pop()
returned_value == 'tomato'
# colors == ['red', 'maroon', 'magenta']
# the Pythonic approach

colors.append('pink')
# add element to the end of the list
# colors == ['red', 'maroon', 'magenta', 'pink']
# the Pythonic approach

colors.extend(['cyan', 'yellow'])
# colors.extend(('cyan', 'magenta', 'yellow'))
# extend the list at the end
# colors == ['red', 'maroon', 'magenta', 'pink', 'cyan', 'yellow']

sum([1, 2, 3, 4, 5])
# add up all the values
# 15

min([1, 2, 3, 4, 5])
# return min value
# 1

max([1, 2, 3, 4, 5])
# return max value
# 5

numbers = (1, 2, 3, 4, 5, 6)
squares = [num ** 2 for num in numbers]
# list comprehensions
# squares == [1, 4, 9, 16, 25, 36]

ind_colors = colors[:]
# create independent copy of the list

import copy
nums1 = [[1, 2], [3, 4]]
nums2 = copy.deepcopy(nums1)
# create deep copy (full copy) of the list

colors.sort()
# sort list in ascending order
# ['cyan', 'magenta', 'maroon', 'pink', 'red', 'yellow']

[7, 23, 9, 6, 7, 123, 0].sort()
# [0, 6, 7, 7, 9, 23, 123]

colors.sort(key=len)
# sort based on item's length
# ['red', 'cyan', 'pink', 'maroon', 'yellow', 'magenta']

def get_second_elem(item):
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_elem)
# sort based on user-defind function
# [(-9, 0), (4, 1), (1, 2)]





