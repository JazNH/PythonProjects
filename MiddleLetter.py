#takes a string and gets the middle char if there is one or blank if there isnt
m = "hello"
l = []
p = " "

#puts each letter into a list
for i in m:
    l.append(i)

#checks to see if the list is even or odd
#if its odd print the middle char
if len(l) % 2 == 0:
    print("")
else:
    k = l[(len(l)-1)//2:(len(l)+2)//2]
    print(p.join(k))
