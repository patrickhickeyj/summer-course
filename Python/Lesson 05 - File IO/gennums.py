import random

# text_to_write = [
# 	"This is a new line of text.\n",
# 	"Here's another line.\n"
# 	"And one.\n"
# ]

# with open('output.txt', 'w') as file:  #----w will overwrite, a will append
# 	for text in text_to_write:
# 		file.write(text)

numholder = []

for i in range(100):
    numholder.append(random.randint(50, 100))

with open('randints.txt', 'w') as file:  #----w will overwrite, a will append
	for text in numholder:
		file.write(f'{str(text)}\n')

