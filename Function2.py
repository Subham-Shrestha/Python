# def add(i,j):
#     print(i+j)
# add(2,3)
# add(8,2)
# add(3,5)

# def info(fn, ln, age): #<----- they are parameters.
#     print(f' Hello {fn} {ln}. You are {age} years old.')
# info('umesh', 'regmi', 29) # <----- they are positional arguments. If position is mismatched, the output becomes incorrect.

# # Keyword arguments.
# def info(fn, ln, age): 
#     print(f' Hello {fn} {ln}. You are {age} years old.')
# info(age = 29, ln = 'regmi', fn = 'umesh') # <----- this is keyword arguments.
# info(ln = 'regmi', age = 29, fn = 'umesh')

#  Default athument. if no value is given, the value is 0.
# def info(fn, ln, age, balance = 0) : 
#     print(f' Hello {fn} {ln}. You are {age} years old.')
#     print(f' your balance iis {balance}')
# info(ln = 'regmi', age = 29, fn = 'umesh', balance = 105)

#  "*args" is meant by arguments
#  "**kwargs" is meant by keyword arguments

# def add(*args):
#     print(args)
# add()
# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4) # args can be called as multiple length positional arguments. it starts with *args and stores value in tuple.

# def add(*args):
#     print(sum(args))
# add(1,2)
# add(2,3,4)

# def add(**kwargs):
#     print(kwargs)
# add(i = 5)
# add(i = 5, j = 10)
# add(i = 5, j = 10, k = 11) # args stores value in tuple and kwargs stores value in dictionary.

def add(i,j):
    return i + j
a = add(2,3); print(add(2,3)) # <----- the value becomes 5
print(a)

# write a function that takes a number as a parameter and returns true if the number is even and false if the number is odd.
# write a function that takes number as a parameter and prints whether the given number is odd or even.
# write a function that takes number and print even number upto that number.