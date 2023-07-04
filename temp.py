import pdb

# testing git branch

l = ['a1', 'a2', 'a3', 'a4','a5']

n = len(l)
print(n) #5

NO_OF_TIME_TO_REPEAT = 3
i = 0
result = list()
print(type(result))

for a in l:
    print(a)
    result = result.append(a)
    print(result)
    pdb.set_trace()

    i += 1
    

    print(result)