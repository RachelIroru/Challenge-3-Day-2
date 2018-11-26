def Fizzbuzz(x, y):
    if not (isinstance(x, list) and isinstance(y, list)):
        return "Invalid input"

    newlist = x+y
    mylist = len(newlist)

    if(mylist % 5 == 0 and mylist % 3 == 0):
        return "Fizzbuzz"

    if (mylist % 5 == 0):
        return "buzz"

    if (mylist % 3 == 0):
        return "Fizz"

    return len(newlist)
