# # error\exception handling
# # they are 3 types 
# # 1.syntax\compile time errors
# # 2.run time errors
# # .logical errors ---> (very difficult to errors) user need to be identified the errors



# #logical errors
# #eg.1 write a simple program of mulitiplication by taking two numbers
# number_1=78
# number_2=48
# result=number_1+number_2  #here code executed but logic was not correct for the multipilcation...
# print(result)

# #logical errrors
# #eg.2 find the addition between two numbers
# number_1=33
# number_2=66
# result=number_1*number_2   #here again logic was not correct
# print(result)

# #syntax errors
# #eg.1
# print(my name is dhanish)

# #eg.2
# def add()
# print(22+25)
# add()

# #eg.3
# num=int(input('enter a number')

# 3.runtime errors

# eg.1
# number1=int(input("enter a number: "))
# number2=int(input("enter a number: "))
# print(number1+number2)
# try:
#  print(number1%number2)
# except:
#     print("some error occured")
# else:
#  print(number1*number2)
#  print(number1-number2)
# finally:
#     print("some operations was completed successfully")

# #eg.2
# number1=int(input("enter a number: "))
# number2=int(input("enter a number: "))
# print(number1+number2)
# try:
#  print(number1%number2)
# except:
#     print("some error occured")
# print(number1*number2)
# print(number1-number2)

# #eg.3:
# my_list=[22,33,44,444,4444,14,24,34]
# print(my_list[0])
# print(my_list[2])
# try:
#  print(my_list[89])
# except:
#     print("some error occured")
# print(my_list[5])
# print(my_list[2])

# #eg.4:
# #eg.3:
# my_list=[22,33,44,444,4444,14,24,34]
# print(my_list[0])
# print(my_list[2])
# try:
#  print(my_list[6])
# except:
#     print("some error occured")
# else:
#  print(my_list[5])
#  print(my_list[2])
# finally:
#     print("these are list operations")

# value error

# #eg.1
# try:
#     num1=int(input('enter the number: '))
#     num2=int(input("enter the number: "))
# except ValueError as k:
#     print(k)
# else:
#     # print(num1+num2)

# #eg.2
# try:
#     age=int(input("enter your age: "))
# except ValueError as k:
#     print(k)
# else:
#     print(age)

# #eg.3
# try:
#     mobile_number=int(input("enter your mobile number: "))
# except Exception as e:
#     print(e)
# else:
#     print(f'your mentioned mobile is {mobile_number}')

# ##typeError
# try:
#     num_1=int(input("enter any number: "))
#     num_2=input('enter any number: ')
#     print(num_1+num_2)
# except TypeError as e:
#     print(e)
    
# #eg.2
# try:
#     num1=44
#     num2='dhanish'
#     print(num1-num2)
# except TypeError as k:
#     print(k)    

# #zero division error
# num1=int(input('enter a number: '))
# num2=int(input('enter a nummber: '))
# try:
#     print(num1/num2)
# except ZeroDivisionError as d:
#     print(d)
    
# #eg.2
# num1=44
# num2=0.00
# try:
#     print(num1/num2)
# except ZeroDivisionError as d:
#     print(d)

# #indexError
# my_list=[12,23,33,44,55]
# print(my_list[0])
# try:
#     print(my_list[10])
# except IndexError as d:
#     print(d)
# print(my_list[2])
# print(my_list[3])


# Exception class (base class for all errors)

# #eg.1
# #indexError
# my_list=[12,23,33,44,55]
# print(my_list[0])
# try:
#     print(my_list[10])
# except Exception as d:
#     print(d)
# print(my_list[2])
# print(my_list[3])

# #eg.2
# try:
#     file=open("dhanish.txt",mode='r')
#     read_data=file.read()
# except Exception as d:
#     print(d)




# filenotfounderror

# eg.1:
# try:
#     file=open("dhanish.txt",mode='r')
#     read_data=file.read()
# except FileNotFoundError as d:
#     print(d)

# #eg.2:
# try:
#     file=open("dhoni.txt",mode='r')
#     read_data=file.read()
# except FileNotFoundError as d:
#     print(d)

 
# #keyword error
# class KeywordError(Exception):
#     pass
# try:
#     keywords = ["class","def","for"]
#     word="clas"
#     if word in keywords:
#         raise
# except KeywordError as e:
#     print(e)
    
    
# #attribute error
# class example:
#     pass
# try:
#     obj=example()
#     print(obj.non_existent_attribute)
# except AttributeError as e:
#     print(e)


# #overflowerror
# import math
# try:
#     result = math.exp(1000)
# except OverflowError as e:
#     print(e)
    

# #inputoutput error
# try:
#     file=open("dem.txt",mode='r')
#     content=file.read()
#     print(content)
# except IOError as e:
#     print(e)

