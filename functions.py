def multiply(a, b):		# function signature
	"""Return the product of two numbers a and b"""

	product = a * b		# function body below
	return product
	print('you can\'t see me')	# won't be executed


print(multiply(2, 6))

help(multiply)


# python scope resolving

# L - local
# E - enclosing
# G - global
# B - built-in

total = 0


def add_to_total(n):
	global total
	total = total + n

add_to_total(8)


