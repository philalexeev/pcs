# while loop samples

n = 1
while n < 5:
    print(n)
    n += 1


num = float(input('enter positive number: '))
while num <= 0:
    print('that\'s not a positive number')
    num = float(input('enter positive number'))


# for loop samples

for letter in 'python':
    print(letter)


for n in range(4):  # will be repeated 3 times
    print('python')


for n in range(4, 7):  # will be repeated 3 times
    print('python')


amount = float(input('enter an amount: '))

for num_people in range(2, 6):
    print(f'{num_people} people: ${(amount / num_people):.2f} each')


# nested loops

for i in range(21):
    for k in range(5, 16):
        print(f'{i} + {k} = {i + k}')


# break / continue statement

for i in range(3):
    if i == 2:
        break
    print(i)    # 0 1

for i in range(3):
    if i == 2:
        continue
    print(i)    # 0 1 3


