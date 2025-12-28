# write a function that takes string as a parameter and returns the reverse of the string.

def reverseString(word) :
    return word[::-1]
a = reverseString(input("Enter a string : "))
print(a)