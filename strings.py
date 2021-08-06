# expected <class 'str'>
type('phil')

name = 'phil'
type(name)


# escape characters
quote = "He said: \"You are idiot\""
quote = "He said: 'You are idiot'"
quote = "He said: 'You're idiot'"


# length of the string
len('my name is')
len(quote)
len(name)


# multiline strings

# doesn't preserve! whitespaces and new lines
song = 'Then it comes to be that the soothing light \
at the end of your tunnel \
Is just a freight train coming your way'

# preserve! whitespaces and new lines
song = """Then it comes to be that the soothing light
at the end of your tunnel
Is just a freight train coming your way""" 


# concatination
name = 'phil'
second_name = 'alexeev'
full_name = name + ' ' + second_name	# expected 'phil alexeev'


# string indexing
band = 'metallica'
band[0] == 'm'
band[3] == 'a'
band[-1] == 'a'
band[-1] == band[len(band) - 1]


# string slicing
band[0:5] == 'metal'
band[:5] == 'metal'
band[5:] == 'lica'
band[:] == 'metallica'
band[-9:-5] == 'meta'
band[-9:] == 'metallica'


# STRING METHODS

'The Great Britain'.lower() == 'the great britain'
'the great britain'.upper() == 'THE GREAT BRITAIN'

'phil      '.rstrip() == 'phil'
'      phil'.lstrip() == 'phil'
'   phil   '.strip() == 'phil'

'metallica'.startswith("meta") == True
'metallica'.startswith("Me") == False
'metallica'.endswith("ca") == True

str_too = input()	# input returns a string
str_too = input('enter some text')

'bla' * 5 == 'blablablablabla'

'2' + '5' == '25'

int('12') == 12
float('12') == 12.0

str(123) == '123'
str(12 + 8) == '20'

long_string = 'very long long example string'
long_string.find('long')	# 5 (onle first occurrence)
long_string.find('phil')	# -1 (no occurrences)
long_string.replace('long', 'short')	# very short short example string (replaced each occurrence)


# f-strings (formatted string literals)
name = 'phil'
age = 54
city = 'Moscow'

# I am phil. I am 54 years old. And I am from Moscow
result = f"I am {name}. I am {age} years old. And I from {city}"











