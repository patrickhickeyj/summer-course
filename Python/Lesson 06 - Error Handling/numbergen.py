import random

with open('numfile.txt', 'w') as f:
    for i in range(100):
        f.write(f'{str(random.randint(1, 1000))}\n')
