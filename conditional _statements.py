# #1.vowel checker.
# '''
# # write a python program that takes a character as input and check whether 
# it is vowel or not.use the if else statement
# '''
# vowels=["a","e","i","o","u","A","E","I","O","U"]
# character=input('enter any character from a-z and A-Z:')
# if character in vowels:
#     print(f"the given character {character}  is vowel")
# else:
#     print(f'the given character {character}  is not vowel')

# #2.age group classification
# '''
# #write a program that takes an age as input and classifies the person into one of the following
# age groups
# .child:0-12years
# .teenager:13-17years
# .adult:18-64years
# .senoir:65years and older
# '''
# age=int(input("enter your age:"))
# if age>0 and age<=12:
#     print(f'your age is {age}years old and your are a child')
# elif age>12 and age<=17:
#     print(f'your age is {age}years old and your are a teenager')
# elif age>17 and age<=64:
#     print(f'your age is {age}years old and your are a adult')
# elif age>64:
#     print(f'your age is {age}years old and your are a senior citizen')

# #3.number classifier
# '''
# write a program that takes an integer as input and classifies it as 
# positive,negative,or zero.use the 
# if elif else statement
# '''
# number=int(input('enter a number:'))
# if number<0:
#     print(f'the given number is {number} is a negative number')
# elif number==0:
#     print(f'the given number is {number} is ZERO/NEUTRAl')
# elif number>0:
#     print(f'the given number is {number} is a positive number')
    
# #4.leap year checker:
# '''
# create a programs that checks whether a given year is a leap year or not..a leap year is 
# divisible by 4,but not by 100 unless it is divisible by 400.
# '''
# year=int(input('enter the year:'))
# if year % 4 == 0 or year%400 ==0:
#     print(f'{year} is a leap year')
# elif year % 100 !=0:
#     print(f'{year} is not leap year')


# #5.calculator
# '''
# build a calculator program that takes two numbers and an operator(+,-,*,/)as input and performs
# as the corresponding operation'''

# number_1=int(input('enter a number:'))
# number_2=int(input('enter a number:'))
# operator=input('choose the operator(+,-,*,/):')

# if operator=="+":
#     result=number_1+number_2
#     print(f'your entered number are {number_1} and {number_2} and you performed addition the result is:{result}')
# elif operator=="-":
#     result=number_1-number_2
#     print(f'your entered number are {number_1} and {number_2} and you performed substraction the result is:{result}')
# elif operator=="*":
#     result=number_1*number_2
#     print(f'your entered number are {number_1} and {number_2} and you performed multiplication the result is:{result}')
# elif operator=="/":
#     result=number_1/number_2
#     print(f'your entered number are {number_1} and {number_2} and you performed division the result is:{result}')
# else:
#     print(f'please choose the correct operator')

# #6.shorthandif
# '''
# rewrite the following code using the short hand 
# if statement
# x=8
# if x%2==0: result="even"
# else="odd"
# '''
# number=int(input('enter a number:'))
# print('even' if number%2==0 else 'odd')

# #7.discount calculator
# '''
# create a program that calculates the final price after applying a discount.the program should take the oroginal
# price and the discount percentage as input
# '''
# original_cost=10000
# product_cost=int(input('enter the product cost:'))
# discount=int(input('enter the discount:'))
# discount_price=product_cost*(discount/100)
# product_cost-=discount_price
# fianl_cost=product_cost
# print(f'the product_cost is {original_cost} and discount is {discount} and the price after discount is {fianl_cost}')

# #8.BMI calculator
# '''
# write a program that calculates that body mass index(BMI) using the formula:BMI=weight(kg)/(height(m)^2).
# the program should take weight and height as input.
# '''
# weight=int(input('enter the weight:'))
# height=int(input('enter the height'))
# BMI=weight/height
# print(f'the weight is {weight}kg and the height is {height}(m)^2 and the BMI is {BMI}kg(m)^2')
