#Palindrome - Write a function palindrome 
# which  takes one argument s as input 
# and returns True if it's a palindrome. 
# False if not
def palindrome(s):
    reversed_sting = str(''.join(reversed(s)))

    if(s == reversed_sting):
        return True
    return False



# Primality - Write a function prime 
# which will take a number n as input
# and return True if n is a prime number
#  and False otherwise
def prime(n):
    number_for_test_prime = int(n)
    if number_for_test_prime < 2:
        return False
    for given_number in range(2, number_for_test_prime):
        if number_for_test_prime % given_number == 0:
            return False
    return True

#Frequency - Write a function called freq 
# which will take a string s as input and 
# return a dictionary of frequencies of each letter in s 
# e.g. freq("aabbbc") will return {'a' : 2, 'b' : 3, 'c' : 1}

def freq(sentance):
    word_and_count ={}
    for letter in sentance:
        word_and_count[letter]=sentance.count(letter)
    return(word_and_count)

# Panagram
def panagram(s):
    s1 = s
    s1.lower()
    s1 = list(set(s1))
    alphabet = list(set("abcdefghijklmnopqrstuvwxyz"))
    count = 0
    i = 0
    while i < len(s1):
        if s1[i] in alphabet:
            count += 1
        i += 1
    if count == 26:
        # print("Is panagram")
        return True
    # print("Is not panagram")
    return False
# s = "The quick brown fox jumps over the lazy dog"
# panagram(s)