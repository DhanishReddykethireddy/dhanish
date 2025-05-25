# '''
# 1.write a pyhton program to calculate the area of a rectangle using the given formula:
# area=length*width.take the values as a user inputs from the user.
# '''
# #area = length * width
# length_of_a_rectangle=float(input("enter the length of a rectangle:"))
# width_of_a_rectangle=float(input("enter the width of a rectangle:"))
# area_of_a_rectangle=length_of_a_rectangle*width_of_a_rectangle
# print(f"the area of a rectangle is length={length_of_a_rectangle} x width={width_of_a_rectangle}, area={area_of_a_rectangle}cm^2")

# #2.write a pyhon progrsm to demonstratre a increment and decrement of a variable
# age=int(input('enter your age :'))
# age*=2
# print(f"after some years your age will be {age}")

# age=int(input('enter your age :'))
# age-=10
# print(f"before 10 years your age was {age} old")

# '''
# #3.write a pythin program to convert temperature from clesius to farenheit.the formula for conversion is 
# F=(c*9/5+32).take the temperature in celsius as input from the user.
# '''
# temepature_in_celsius=float(input('enter the temperature:'))
# temparature_in_farenheit=(temepature_in_celsius*9/5+32)
# print(f'the temperature in celsius is {temepature_in_celsius} and temperature in forenheit is {temparature_in_farenheit}')

# #4.write a python program to calculate simple intrest given the principal amount,rate and time(in years)
# #si=ptr/100
# principal_amount=int(input('enter the given amount:'))
# time=int(input('enter how many years completed:'))
# rate=int(input('enter how much rate:'))
# simple_interst=principal_amount*time*rate/100
# principal_amount+=simple_interst
# print(f'the simple intrest for the principal amount is {simple_interst} and the total amount have to get {principal_amount}')

# #5.write a python program to concatenate two strings and display the result.the strings should be taken as an input from the user
# wishes=input('enter wishes:')
# name=input('enter your name:')
# print(wishes + name)

# village=input('enter your village name:')
# district=input('enter your district name:')
# print(village+district)

# #6.write a pyton program to convert a distance from kilometers to miles
# kilometres=float(input('enter the distance travlled in kms:'))
# miles=kilometres*0.62137119
# print(f'the distance you travlled in kilometres is {kilometres}kms and that in miles is {miles}miles')

# #7.create a program that takes user input  for their name and age.use formatted strings to print a message welcoming the user and stating their age
# name=input("enter your name:")
# age=int(input("enter your age:"))
# print(f"hii mr/ms {name} happy birthday to you and congratulations you turned into {age} years old")

# #8.write a python script that defines a dictinary with information about a product (eg:name,price,quantity).use formatted strings to display the information in a readbale format
# dictionary={
#     "product":"mobile",
#     "brand":"vivo",
#     "price":55000,
#     "store":"sangeetha"
# }
# print(f'the product type is {dictionary["product"]}')
# print(f'the brand of the product is {dictionary["brand"]}')
# print(f'the price of the product is {dictionary["price"]}rupees')
# print(f'the product that i bought from {dictionary["store"]} store ')

# #9.create a list called numbers from 1 to 10 
#     # .check if number 5 is in list
#     # .check the number 15 is not in the list.
# numbers=[1,2,3,4,5,6,7,8,9,10] 
# print(5 in numbers)   
# print(15 not in numbers)

#10.
