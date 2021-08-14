# booleans True / False

1 < 2   # True
1 > 2   # False
'st' == 'st'    # True
'st' != 'er'    # True

not True == False   # True
False == not True   # ERROR (because of operator precedence)
False == (not True) # True


# if / elif / else

n = 75

if n > 90:
    print('first')
elif n > 80:
    print('second')
elif n > 70:
    print('third')
else:
    print('other')


# try / except

try:
    num = int(input('please enter the valid number'))
except ValueError:  # or (ValueError, TypeError)
    print('invalid value was entered')


try:
    num = int(input('please enter the valid number'))
except ValueError:
    print('invalid value')
except TypeError:
    print('invalid type of value')
