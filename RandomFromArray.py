# Using the random import to look through an array and by using random.choice it will pick something
# from the array to display
import random

friends = ["Spongebob", "Patrick", "Sandy", "Squidward", "Plankton", "Mr.Krabs"]

selected = random.choice(friends)
print("Go talk to: " + selected)
