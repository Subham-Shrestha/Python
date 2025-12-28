# write a function that takes a string as parameter and returns the first vowel present in that string.
def find_first_vowel(vow):
    for check in vow:
        if check in 'aeiouAEIOU':
            return check

find_first_vowel('Ram, Shyam, Sita, Hari')
