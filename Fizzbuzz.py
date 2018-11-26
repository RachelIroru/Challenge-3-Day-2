def Fizzbuzz(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        return "Invalid input"

    newlist = a+b
    mylist = len(newlist)

    if(mylist % 5 == 0 and mylist % 3 == 0):
        return "Fizzbuzz"

    if (mylist % 5 == 0):
        return "buzz"

    if (mylist % 3 == 0):
        return "Fizz"

    return len(newlist)
