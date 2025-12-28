# write a function that takes multiple numbers as parameter and returns the mean of those numbers.

def meanNumber(*args):
  mean = sum(args) / len(args)
  return mean
average_value = meanNumber(1, 2, 3, 4, 5, 6)
print(average_value)

# lentgh = int(input("Enter length of numebrs : "))
# def meanNumber(*args):
#     for args in lentgh :
#      numebrs = int(input("Enter the numbers : "))
#   mean = sum(numebrs) / len(lentgh)
#   return mean
# average_value = meanNumber(1, 2, 3, 4, 5, 6)
# print(average_value)
