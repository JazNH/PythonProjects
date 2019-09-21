seven = 7
counter = 0
x = input('Give me a whole number')
copyOfX = [int(i) for i in str(x)]

for i in copyOfX:
    if (seven == i):
        counter = counter + 1

print ('There are ' + str(counter) + ' in ' + str(x))