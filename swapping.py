# #fibonacci series

##without using a function
# a=0
# b=1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c) 
 
# #with using function    
# n=int(input("enter a number:"))
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         global a,b
#         c=a+b
#         a=b
#         b=c
#         print(c,end =" ")
# fibonacci(n)

# #factorial sequence

# #with using function
# n=int(input("enter a number:"))
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))

# #without using function
# m=int(input("enter a number:"))
# result=1
# for i in range(1,m+1):
#     result*=i
# print(result)

# #palindrome function:
# number1=int(input("enter a number:"))
# number2=int(input("enter a number:"))
# for i in range(number1,number2):
#     j=str(i)[::-1]
#     j=int(j)
#     if i ==j:
#         print(i,'is a palindrome') 
#     else:
#         print(i,'not a polindrone')   
        
# #checking a number is palindrome or not
# number=int(input('enter a number:'))
# dhanish=str(number)[::-1]
# dhanish=int(dhanish)
# if number==dhanish:
#     print(number,"is a polindrome")
# else:
#     print(number,"is not a polindrome")


# #factorial series ==>returns n*n-1 numbers
# number=int(input("enter a number:"))
# result=1
# for i in range(1,number+1):
#     result*=i
#     print(result)
# print(f'the factorail of {number} is {result}')

# #with function
# number=int(input('enter a number:'))
# def factorial(number):
#     if number==0:
#         return 1
#     else:
#         return number*factorial(number-1)
# print(factorial(number))
        
# #factorial
# #with out using function
# number=int(input('enter a number:'))
# result=1
# for i in range(1,number+1):
#     result*=i
# print(result)

# #with fnction
# n=int(input("enter a number:"))
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))


# #fibonacci series()
# #without function
# a=0
# b=1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ')

# #with function
# n=int(input("enter a number:"))
# a=0
# b=1
# def febonacci(n):
#     for i in range(n):
#         global a,b
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
# febonacci(n)

# #palindrome
# #checking palindrome or not
# number=int(input("enter a number:")) #10
# dhanish=str(number)[::-1] #01
# dhanish=int(dhanish) #01
# if number==dhanish:#10==01  false
#     print(f'{number} is a palindrome')
# else:
#     print(f'{number} is not a palindrome')
    
# #finding palindrome from 1 to 100
# n1=int(input("enter a number1:"))
# n2=int(input("enter a number2:"))
# for i in range(n1,n2+1):
#     j=str(i)[::-1]
#     j=int(j)
#     if i == j:
#         print(i)
        
# #using function
# n=int(input("enter a number:"))
# def palindrome(n):
#     return str(n)==str(n)[::-1]
# print(palindrome(n))

# #from 10 to 100
# def palindromes(n,m):
#     for i in range(n,m+1):
#         j=str(i)[::-1]
#         j=int(j)
#         if i == j:
#             print(i,end=" ")
# print(palindromes(1,100))


import functions
from functions import *
print(add(23,27))
print(mul(22,2))
print(div(22,2))
