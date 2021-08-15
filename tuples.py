# tuples
# tuples are immutable

tup = (1, 2, 3) # tuple sample
type(tup)   # <class 'tuple'>
empty_tuple = ()
one_el_tuple = (1,)

# create tuple from any sequence type -> ('p', 'y', 't', 'h', 'o', 'n')
tup = tuple('python')

# methods

# length of the tuple
len(tup)  # 3
tup[3]    # h

# slicing
tup_slice = tup[:3]
print(tup_slice)    # ('p', 'y', 't')

# looping
for char in tup:
    print(char.upper())

# packig into single tuple
coords = 4.03, 6.77
print(coords)   # (4.03, 6.77) -> tuple

# unpacking from tuple
x, y = coords
print(x)    # 4.03
print(y)    # 6.77

# multiple variables assignment
a, b, c = 'string', 23, ('q', 'w', 'e')
print(a)    # 'string
print(b)    # 23
print(c)    # ('q', 'w', 'e')

print('p' in tup)   # True
print('e' in tup)   # False

num1 = 8
num2 = 5

adder_subtractor = (num1 + num2, num1 - num2)
print(adder_subtractor)
