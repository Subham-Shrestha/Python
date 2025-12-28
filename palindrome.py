# write a function that takes string as a parameter and checks the string is palindrome or not. Disregarding case sensitivity.

def palindrome(word):
    if word[::-1] == word:
        print(f'{word} word is palindrome.')
    else:
        print(f'{word} word is not palindrome.')

palindrome(input("Enter a string: "))