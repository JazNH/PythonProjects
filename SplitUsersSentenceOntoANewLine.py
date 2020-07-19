#Taking a users sentence and returning all the words into a new line

#Asking for the users input and putting it into a variable called "text"
text = input("Type a sentence you want to be split: ")

#Spliting the word and putting it into a variable called "wordNeedToSplit"
wordNeedToSplit = text.split()

#looping and printing all the words in a sentence
for word in wordNeedToSplit:
    print(word)