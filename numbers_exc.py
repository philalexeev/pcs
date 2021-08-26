int('25')	# 25
float('25.5')	# 25.5
type(25)	# <class int>
type(25.0)	# <class float>

1000000 == 1_000_000	# True (check why it cause syntax error)
1e6 == 10000000.0
2e+4 == 20000.0
2e-4 == 0.0002
2e400	# inf
-2e400	# -inf

# adding
1 + 1 == 2
1 + 1.0 == 2.0

# substraction
7 - 5 == 2
7 - 5.0 == 2.0
7 - (-3) == 10

# multiplying
2 * 3 == 6
2 * 3.0 == 6.0

# division
6 / 3 == 3.0
6 / 3.0 == 3.0

# integer division (floor division)
5 // 2 == 2
5.0 // 2 == 2.0

# exponents
2 ** 2 == 4
2 ** 3 == 8
2 ** 4 == 16

# modulus operator
5 % 3 == 2
20 % 7 == 6
16 % 8 == 0
5 % -3 == -1

# to calculate the remander r of dividing a number x by a number y, Python uses the equation
r = x - (y * (x // y))

# math functions

round(2.3) == 2
round(2.7) == 2

# rounding ties to even (round .5 fpn)
round(2.5) == 2
round(3.5) == 4

round(3.15483, 3) == 3.155

round(3.15483, 1.4)	# TypeError (the second argument must be an integer)
round(2.675, 2) == 2.67	# o0 ieee


abs(3) == 3
abs(-3) == 3
abs (-2.7) == 2.7

pow(2, 3) == 8
pow(4, 3) == 64

# pow(x, y, z) == (x ** y) % z
pow(2, 3, 2) == 0
pow(4, 3, 7) == 1


# methods

2.4.is_integer() == False
2.0.is_integer() == True

# printing in style in results of f-string

n = 1.347
f'{n:.2f}' == '1.35'
f'{n:.4f}' == '1.3470'

n = 1234567890
f'{n:,}' == '1,234,567,890'

n = 12345.67
f'{n:,.2f}' == '12,345.67'









