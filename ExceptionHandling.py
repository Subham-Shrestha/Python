#  Bugs : fault/ errors in programs are called Bugs
#  Three types if bugs :
# --> Syntax error, --> Logical error, --> Runtime error
# Syntax error :
# -> Occurs because of typo.
# -> If you write code that python compiler does not understand then type error occurs.
# -> print('Hello) is the syntax error.
# -> The program won't be executed when there is syntax error.
# print("Hello world.")
# print("Hello world.")
# print("Hello world.")
# print("Hello world.")
# print("Hello world.")
# print('Hello world)
# print("Hello world.")
# print("Hello world.")

# while True :
#     age = int(input("Enter age : "))
#     if age < 18 :
#         print("You can vote.")
#     else : 
#         print("You cannot vote.") -> Logical error : Logical error runs but the expected output is not got.
# Runtime Error / Exceptions :
# while True :
#     try :
#         fn = int(input("Enter first numebr : ")) 
#         ln = int(input("Enter last number : "))   # 0 crashes the program. The program terminates unexpectedly.
#         print(fn / ln)   
#     except Exception as e :
#         print(type(e))
#   Everytime runtime error shall be checked. To ignore the error, use
# try :
#   #risky code
#  Code that can throw errors is risky code.
# except :
#   #alternative code
#   #code to run when there is an error.
# It is good to put all the code inside try.
# while True :
#     try :
#         fn = int(input("Enter first numebr : ")) 
#         ln = int(input("Enter last number : "))   
#         print(fn / ln)  
#     except ZeroDivisionError :
#         print("Second number cannot be 0.")
#     except ValueError :
#         print("Inputs must be number.")
#     except :
#         print("An error occured.")