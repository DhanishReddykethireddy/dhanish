# #def fumction
# def addition():
#     a=25
#     b=87
#     c=a+b
#     print(c)
# addition()

# def substraction():
#     my_fatherage=50
#     my_uncleage=74
#     myage=my_uncleage-my_fatherage
#     print(myage)
#     print(f'my age is {myage}')
# substraction()

# #return statement  
# def multiplication(a,b):
#     return a*b
# print(multiplication(20,22))    

# def division(c,d):
#     return c/d
# print(division(888,3))

# #default parameters ==> it wont show errors by declaring default parameters in the operation
# def dhanish(a=1,b=1,c=1):
#     return a*b*c
# print(dhanish(22))
# print(dhanish(22,34))
# print(dhanish(22,34,23))

# def krish(a=None,b=None,c=None):
#     return "Company:",a,  "Role:",b, "Name:",c
# print(krish('wipro','pythondeveloper','dhanish reddy'))


# #arbitary arguements ==>by using this we can add bulk data or simple we can say it will  throws 
# # output in tuple format
# def tuple(*k):
#     return k
# print(tuple('dhanish','krish','freeire',24))

# def bhanu(*K):
#     return K
# print(bhanu("bhanu prakash",24,'cartoons'))

# #keyword arguements ==>it wills throws output in key value pair and it wills out put same like dictionary
# def ramachandra(**r):
#     return r
# print(ramachandra(name='dhanish',age=24,profession='pythondeveloper'))

# def harish(**d):
#     return d
# print(harish(favbike='pulsar',favwork='farming',favvillage='diguvapalli'))

# #local and global variables
# def greet():
#     name=input('enter the name:')#name is a local variable because we cannot acess outside the function
#     print(f'hii {name},good morning {name}')
# greet()

# balance=1500#global variable we can acess the variable outside the function also
# def credit(amount):
#     return amount+balance    
# print(credit(500))
# print(balance)

# balance=10000
# def credit(amount):
#     global balance  #we need to declare global and variablename when we perform operation in an function
#     balance+=amount
#     print(balance)
# credit(10000)
    

#calculator program
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div (a,b):
    return a/b
def mod(a,b):
    return a%b
def fldiv(a,b):
    return a//b
def expo(a,b):
    return a**b

# # #inbuilt methods
# import math 
# # for i in range(1,37):
# #      print(i,math.sqrt(i))
# # for i in range(1,10):
# #     print(i,math.pow(i,5))
# print(math.pi)

# '''
# task.1:add function
# write a python funtion named add that takes two arguements a and b and returns sum
# '''
# def add(a,b):
#     return a+b
# print(add(23,89))

# '''
# task.2:square function
# write a python function named square that takes a number x as input and returns square
# '''
# def square(x):
#     return x*2
# print(square(4))

# '''
# task.3:factorial function 
# write a python function named factorial that takes a positive integer n as input and returns its 
# factorial
# '''
# #finding factorial without using function
# n=int(input("enter a number:"))
# result=1
# for i in range(result,n+1):
#     result*=i
# print(result)

# #finding factorial with function
# n=int(input("enter a number:"))
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))

# '''
# task.4:maximum number
# write a python function named maximum that takes a list of numbers as input and returns the maximum
# value in the list
# '''
# #finding max number in a list without using functions
# #finding max number by negative indexing
# numbers=[23,54,654,3456,8976,1234445,87575656]
# numbers.sort(reverse=True)
# print(numbers[0])

# #finding max number by positive indexing
# numbers=[87834,63738,783786,84887867,98739873,7386838]
# numbers.sort()
# print(numbers[-1])

# #max number by finding with function
# numbers=[23,45,98,45,234,444,598]
# def maximumnumber(numbers):
#     return max(numbers)
# print(maximumnumber(numbers))

# '''
# task.5:reverse function
# write a python function named reverse that takes a string s as input and returns its reverse
# '''
# s=input("enter a string:")
# def reverse(s):
#     return s[::-1]
# print(reverse(s))

# '''
# task.6:check prime function
# write a python function named is_prime that takes a positive integer n as input and returns true n is prime,
# otherwise false
# '''
# #finding prime numbers from 1 to 150 and finding length also and finding 4th prime number in that series
# prime_numbers=[]
# for i in range(1,151):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             prime_numbers.append(i)
# print(prime_numbers)
# print(len(prime_numbers))
# print(prime_numbers[3])

# #using function for finding prime numbers
# a=int(input("enter starting number:"))
# b=int(input("enter end point:"))
# prime_numbers=[]
# def prime():
#     global prime_numbers
#     for i in range(a,b+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")
#             prime_numbers.append(i)
#     print(prime_numbers)
# prime()

# #to check whether the given number is a prime or not
# number=int(input("enter a number:"))
# def is_prime():
#     global number
#     for i in range(2,number):
#         if number %i==0:
#             print(number,"is not prime")
#             break
#     else: 
#         print(number,'is prime')
# is_prime()
        
# '''
# task.7:fibonacci function function
# write a python function named fibonacci that takes a positive integer n as input and returns nth fibonacci number
# '''
# n=int(input('enter a positive integer:'))
# def fibonacci():
#     global n
#     a=0
#     b=1
#     for i  in range(n+1):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=' ')
# fibonacci()
    
# '''
# # # task.8:palindrome function
# # # write a python function named is palindrome that takes a string s as input and returns true if s is a palindrome,
# # # otherwise false'''
# s=input('enter a name:')
# def palindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(palindrome(s))

# '''
# task.9:sum of squares function
# write a python function named sum_of_squares that takes a list of nummbers as input and return the sum of the 
# squares of those numbers
# '''
# numbers=[2,3,4,5,6]
# result=0
# def sum_of_squares():
#     global result
#     for i in numbers:
#         result +=i*i
#     print(result)
    
# sum_of_squares()

# '''
# task.10:average function
# write a function named average that takes a list of numbers as input and returns average value
# '''
# list=[23,24,25,26,27,28]
# def average():
#     global list
#     sum_of_elements=sum(list)
#     len_of_list=len(list)
#     average=sum_of_elements/len_of_list
#     print("average",average)
# average()
