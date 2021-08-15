# tuples
# tuples are immutable

tup = (1, 2, 3) # tuple sample

type(tup)   # <class 'tuple'>

empty_tuple = ()

one_el_tuple = (1,)

# create tuple from any sequence type -> ('p', 'y', 't', 'h', 'o', 'n')
new_tuple = tuple('python')


# methods

len(new_tuple)  # 3

new_tuple[3]    # h

tup_slice = new_tuple[:3]
print(tup_slice)    # ('p', 'y', 't')


