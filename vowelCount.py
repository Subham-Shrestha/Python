# write a function that takes a string as parameter and returns the total number of vowels present in that string.
def count_vowels(vowel):
    count = 0
    for counter in vowel.lower():
        if counter in 'aeiou':
            count = count+1

    return count

# print(count)