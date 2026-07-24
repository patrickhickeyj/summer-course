min = 10000
max = 0
count = 0
sum = 0


with open('numfile.txt', 'r') as f:
    lines = f.readlines()
    rawvar = [line for line in lines]
    testvar = [int(line) for line in lines]
    for line in lines:
        numhold = int(line)
        count += 1
        sum += numhold
        if numhold > max:
            max = numhold
        if numhold < min:
            min = numhold

av = sum / count

print(rawvar)
print(testvar)

print(f'The min is {min}, the max is {max}, the average is {av}')