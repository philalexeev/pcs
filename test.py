import random


def coin_flip():
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'


heads_tally = 0
tails_tally = 0

for i in range(10_000):
    if coin_flip() == 'heads':
        heads_tally += 1
    else:
        tails_tally += 1

print(f'the ratio of heads to tails is {(heads_tally / tails_tally):.2f}')
