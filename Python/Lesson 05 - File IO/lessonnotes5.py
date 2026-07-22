# def getinterest(principal, rate, years, num = 1):
#     result = principal * (1 + (rate / num)) ** (num * years)
#     return result

# print(getinterest(1000, .031, 10))

#----------Reading/writing-----------

# with open('input.txt', 'r') as file:
# 	lines = file.readlines()
# 	for line in lines:
# 		print(line)
		
# text_to_write = [
# 	"This is a new line of text.\n",
# 	"Here's another line.\n"
# 	"And one.\n"
# ]

# with open('output.txt', 'w') as file:  #----w will overwrite, a will append
# 	for text in text_to_write:
# 		file.write(text)

testlines = 'blank'
tester = 'blank'

with open('input.txt', 'r') as f:
    # testlines = f.readlines()
    tester = f.read()


print(tester)
print(testlines)