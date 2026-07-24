
def testfunc():
    print('error')

numvar = [1, 2, 3]

testvar = 5

mydict = {
    'name' : 'value',
    'name2': 'value2'
}
print(mydict['name'])

with open('notfile.txt', 'r') as f:
    ervar = f.readlines()
    print(ervar)