#takes a word and checks to see how many capital letters are in it
word = input("Give me a word: ")
list = []
finalList = []

#puts every letter into the list variable
for letter in word:
    list.append(letter)

#takes the index and value and if the value is uppercase
#then add the index of that value to the final list
for idx, val in enumerate(list):
    if val.isupper():
        finalList.append(idx)

print(finalList)
