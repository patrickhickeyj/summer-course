min = 100
max = 50
sum = 0
iterator = 0


with open('randints.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		inthold = int(line)
		if inthold > max:
			max = inthold
		if inthold < min:
			min = inthold
		sum += inthold
		iterator += 1
		
average = sum / iterator

print(f'min is {min}, max is {max}, average is {average}')