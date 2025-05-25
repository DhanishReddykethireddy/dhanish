# # # 1.lambda function()
# # # 2.filter function()
# # # 3.map function()
# # # 4.reduce function()
# # # 5.generator function()

# # #1.lambda function()
# # #syntax
# # #lambda expression:iterable
# # add=lambda a,b:a+b
# # print(add(10,34))

# # mul=lambda a,b:a*b
# # print(mul(5,4))

# # div=lambda k:k%4
# # print(div(20))

# # #2.filter function()
# # #syntax
# # #filter(function,iterable)
# # whole_numbers=[1,2,3,4,5,6,7,8,9,10]
# # def even(i):
# #     return i%2==0
# # even_numbers=filter(even,whole_numbers)
# # print(list(even_numbers))               #method 1

# # even=filter(lambda i:i%2==0,[11,12,13,14,15,16,17,18,19,20])
# # print(list(even))

# # square=filter(lambda k,:k**2 <=1000,[11,13,18,4,21,31,41,51,61])
# # print(list(square))

# # #3.map function()
# # #syntax
# # #map(function,iterable,......)
# # add=map(lambda x,y:x+y,[1,2,3,4],(1,2,3,4))
# # print(list(add))

# # mul=list(map(lambda a,b:a*b,[23,33,44,444],[2,3,4,44]))
# # print(mul)

# # uppertolower=map(lambda i,j:i+j,['CAT','BAT','RAT'],['AND','NOT','NOT IN'])
# # print(list(uppertolower))

# # sub=map(lambda a,b:b-a,[787,686,545],[797,786,745])
# # print(list(sub))

# # add = map(lambda a,b,c,d,e:a+b-c*d+e,[2222,4244],[22,44],[32,31],[21,22],[31,32])
# # print(list(add))

# # #4.reduce function()
# # #syntax
# # #from functools import reduce
# # #syntax
# # #reduce(function,iterable,[intializer])==>intializer is optional
# # from functools import reduce
# # result=reduce(lambda a,b:a+b,[23,24,25,26,27,28])
# # print(result)

# # mul=reduce(lambda a,b:a*b,(1,2,3,4,5,6,7))
# # print(mul)

# # sub=reduce(lambda a,b:a-b,[98989,8786,746,76])
# # print(sub)

# # #5.generator function()
# # #syntax
# # #def keyword():
# #         #yield 1
# #         #yield 2
# #         #yield 3

# # def num(a,b,c):
# #     yield a+b+c
# #     yield a-b-c
# #     yield a*b*c
# # sample=num(44,22,11)
# # print(sample.__next__())
# # print(sample.__next__())
# # print(sample.__next__())
        
# # #coding exercises
# # '''
# # 1.write a pythoon function  square all (numbers) that takes a list of numbers as input and
# # returns a new list containing the square of each  number in the input list.use map function()
# # with lambda  function () to implement this
# # '''
# # square_all=map(lambda a:a*a,[11,12,13,14,15,16,17])
# # newlist=print(list(square_all))

# # '''
# # 2.write a python function filter positive(numbers) that takes alist of numbers as input and
# # returns a new list containing only positive numbers from the input list.use the filter function
# # to implement this..'''
# # numbers=filter(lambda a:a>0,[-23,373,973,-7633,-2673,753,8637,-647,7673,444,22,134,-789])
# # positive_numbers=print(list(numbers))

# # '''
# # 3.write a python function calculate factorial(n) that calculates the factorial of a given number
# # n.use the reduce function() with an appropriate lambda function to implement this
# # '''
# # from functools import reduce
# # n=int(input('enter a number:'))
# # def calculate_factorial(n):
# #     if n ==0:
# #         return 1
# #     else:
# #          return reduce(lambda a,b:a*b, range(1,n+1),1)
# # print(calculate_factorial(n))

# '''
# 4.write a pyhton function count vowels(string) as input and returns  the count of vowels
# (a,e,i,o,u) in the input string.use the reduce() function with an appropriate lambda function to
# implent this
# '''
# from functools  import reduce
# string=input("enter astring:").lower()
# vowels=['a','e','i','o','u']
# def countvowels(string):
#     return reduce(lambda count,characters:count+(characters in vowels),string, 0)
# print(countvowels(string))

# from functools import reduce
# string='hello dhanish,good morning'.lower()
# vowels_count=reduce(lambda count,character:count+(1 if character in 'aeiou' else 0),string,0)
# print(vowels_count)  
    