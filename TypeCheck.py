# Checks the type of the inputting parameters and returns true if int and false if other
def only_ints(x, y):
    if type(x) == int and type(y) == int:
        print("True")
        return True
    else:
        print("false")
        return False

only_ints("s",2) #False
only_ints(2,"s") #False
only_ints("s","s")#False
only_ints(2,2) #True
only_ints(-2,2) #True
only_ints(-2,-2) #True
only_ints(2,-2) #True
only_ints(2,True) #False
only_ints(2,False)#False
only_ints(True,2) #False
only_ints(False,2) #False
