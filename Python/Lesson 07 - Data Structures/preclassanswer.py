numholder = []

with open('preclass_problem1_data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        numholder.append(int(line))

numholder.sort()

last5 = numholder[-5:]
print(last5)

total = 0

for i in range(len(last5)):
    total += last5[i]

print(total)
answer = total/10

print(f'The answer is {answer}')