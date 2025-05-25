#1.write a pyhton program that prints your name
name=input('Enter your name:')

#2.comments
#performing addition
number_1=int(input('enter a number:'))
number_2=int(input('enter a number:'))
result=number_1+number_2
print(f'the addition of two  numbers is:{result}')
'''
writing a program to 
ask the user detials
'''
name=input('what is your name?:')
age=int(input('what is your age?:'))
weight=float(input('what is your weight?:'))
height=float(input('what is your height?:'))

#3.define a list containing three different data types
list_1=[1,2,3,1,2,3,(1,2,3),{"name":"dhanish","age":24},{23,56,44},"sandhya",5.7,[24,25,26]]
print(type(list_1))
print(id(list_1))
print(list_1)

#4.string operations
#concatente 2 strings and print the result
name=input("Enter your first name:")
last_name=input("enter your last name:")
full_name=name+last_name
print('f'"your name is:",{full_name})  #concatenation
#repeat a string 3 times  and print output
name="dhanish"
repeated_name=name*3
print(repeated_name)

#5.python keywords
#create a varaible with a name that is python keyword.what happens
# if="python_keyword"
# print(if)

# 6.pyhton variables
# declare two variables,one is storing an integer and other a string print their values
age=int(input('enter your age:'))
print(type(age))
print(age)
name=input('enter your name:')
print(type(name))
print(name)

#7.type conversion
#convert a float to an integer and print the result
height=5.89
print(type(height))
int_conversion=int(height)
print(int_conversion)
#convert an integer toa string and diplay the output
age=24
print(type(age))
string_conversion=str(age)
print(string_conversion)
print(type(string_conversion))

#8.sample input and output
#take user's age as input and print a message using that input
user_age=int(input('enter your age:'))
print(f'your mentioned age is : {user_age}')
    
        #exercise
#1.print statement
# write a program that prints a pattern using multiple print statements
print('   $   ')
print('  **   ')
print(' ****  ')
print('*******')
print(' ****  ')
print('  **   ') 
print('   $   ')

#2.create a python script for a simple task and add comments to exlain each step
"""
basic detials
of a customer
"""
name=(input("enter your name:"))#name of the customer
produt=(input('choose the products(laptop,mobile,refrigirator,tv,etc):'))#asking about the product
cost_of_product=(float(input('mention the cost of the product:')))#gettig about the cost of the 
print('tq for visiting our shop,please come again')
#3.data structures and data types
#implement a program that uses a dictionary to store information about a book(title,author,publication year)
book={
    "title":"bhagavad gita",
    "author":"maharsi vedavyasa",
    "language":"sanskrit",
    "chapters":18,
    "verses":700,
    "published_year":"1st or 2nd century" 
}
print(book)
print(id(book))
print(type(book))

#4.string operation
#write a python program that takes a string as input(35) and return float value
number=input('enter a number:')
print(type(number))
float_conversion=float(number)
print(type(float_conversion))
print(float_conversion)

#5.concatenate strings
#write a pyhton to take two names as input and print them together
student_name="ram gopal"
fathers_name="varma"
print(student_name+fathers_name)

#6.type conversion
#create a program tha takes user input for their age,converts it into an integer,adds 5,and then prints result
suhash_age=int(input('enter your age:'))
sharath_age=suhash_age+5
print(sharath_age)

#7.simple input and output
#build a calculator program that takes two numbers as input and perform the arithmetic operation
number_1=int(input('enter a number1:'))
number_2=int(input('enter a number2:'))
print(number_1+number_2)
print(number_1-number_2)
print(number_1*number_2)
print(number_1/number_2)
print(number_1%number_2)

    #8.type conversion
#1.dictionary to tuple
book={
        "title":"she loves her",
        "author":"sadhya",
        "chapters":24, 
}
print(book)
print(type(book))
tuple_conversion=tuple(book)
print(tuple_conversion)

#2.tuple to dictionary
tuple_1=(("name","dhanish"),("age",24),("height",5.7),)
print(type(tuple_1))
dict_conversion=dict(tuple_1)
print(dict_conversion)
print(type(dict_conversion))

#3.list to set conversion
list_1=[1,2,3,"dhanish","sandhya",78.4,22.56,(1,2,3),(1,2,3)]
print(type(list_1))
set_conversion=set(list_1)
print(set_conversion)
print(type(set_conversion))

#4.set to tuple conversion
set_1={4,5,6,88.9,"harish","krish",(12,34,55.67)}
print(set_1)
print(type(set_1))
tuple_conversion=tuple(set_1)
print(tuple(set_1))
print(type(tuple_conversion))

#5.set to list conversion
set_1={11,12,13,44.4,55.5,"dhanish","sandhya",(23,56,99)}
print(set_1)
print(type(set_1))
list_conversion=list(set_1)
print(list_conversion)
print(type(list_conversion))