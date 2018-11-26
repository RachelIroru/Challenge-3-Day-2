vowels = 'aieou'
string = input('Input any word of your choice:')
Rachel= []
def get_vowels(): #get the vowels from the word given
    count = len(string) #return the number of vowels in the container
    if count > 0:
        for letter in string:
            if letter in vowels: 
                Rachel.append(letter) #append means to add a letter at the end
        return tuple (Rachel) #tuple is an argument; return tuple means that return vowel
    else:
        return'()'
print(get_vowels())   
