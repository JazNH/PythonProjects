#takes a dictionary and tells you how many people are online
dict = ({'Alice': 'online', 'Bob': 'online', 'Cindy': 'offline'})
count = 0;

#looks at each item in the dictionary and if the value is online then increase the counter
for i in dict:
    if format(dict[i]) == "online":
        count = count + 1

print(count)