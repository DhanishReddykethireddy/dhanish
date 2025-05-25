# #1.sum of squares
# '''
# write a python program that calculates and prints the sum of squares of numbers from numbers
# 1 to 5 using a for loop'''
# sum_of_squares=0
# for i in range(1,6):
#     print(i*i)
#     sum_of_squares+=i*i
# print(f'sum_of_squares from 1 to 5 is {sum_of_squares}')

# #a.sum of cubes from 1 to 10
# cubes_sum=0
# for i in range(1,11):
#     print(i**3)
#     cubes_sum+=i**3
# print(f'the sum of cubes from 1 to 10 is {cubes_sum}')

# #2.countdown
# '''
# write a python program that uses a while loop count from 5 to 1
# '''
# number=5
# while number>0:
#     print(number)
#     number-=1

# #from 1 to 10
# age=1
# while age<11:
#     print(age)
#     age+=1    
    
# #3.multiplication table with nested for loop
# '''
# write a python program to print the multiplication table for a 
# user speicified number using a nested  for loop'''
# table=int(input('enter the number of the table which you want:'))
# for i in range(1,11):
#     print(f'{table} X {i} = {table*i}')

# '''4.write a python program that uses a for loop to find sum of all even numbers 
# between 0 and 10 (inclusive)
# '''
# even_numbers_sum=0
# for i in range(0,11,2):
#     print(i)
#     even_numbers_sum+=i
# print(f'sum of even numbers from 1 to 10 is {even_numbers_sum}')

# # sum of odd numbers from 1 to 50
# odd_sum=0
# for i in range(1,51,2):
#     print(i)
#     odd_sum+=i
# print(f'the odd sum fro 1 to 50 is {odd_sum}')

# #5.calculate the sum of all numbers from 1 to a given number
# number=int(input("enter a number:"))
# sum_of_numbers=0
# for i in range(1,number+1):
#     print(i)
#     sum_of_numbers+=i
# print(f'sum of all numbers from to given number is {sum_of_numbers}')

# #6.display numbers from a list using a loop
# employees_salary=[10000,13500,15000,16500,19000,21000,44000]
# print(type(employees_salary))
# print(id(employees_salary))
# print(employees_salary)
# for i in employees_salary:
#     print(i)

# #7.display numbers from -10 to -1 using for loop

# for i in range(-10,0):
#     print(i)

# #8.write a program to display all prime numbers within a range
# number_1=int(input('enter a number_1:'))
# number_2=int(input('enter a number_2:'))
# for num in range(number_1,number_2+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#          print(num)
