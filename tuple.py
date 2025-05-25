# #tuple creation
# tuple=(1,2,3,"dhanish","sandhya",[12,13,14])
# print(type(tuple))

# #tuple built in functions
# #1.length
# tuple=(1,2,3,"dhanish","sandhya",56.7)
# print(len(tuple))

# #2.all function
# tuple=(1,2,3,"dhanish","sandhya",56.7)
# print(all(tuple))

# set=(22,23,25,0,234,567)
# print(all(set))

# tuple1=(False,'dhanish','sandy',123,456)
# print(all(tuple1))

# #3.index()
# dhanish=(1,2,3,"dhanish","sandhya",[12,13,14])
# print(dhanish[5])
# print(dhanish[::-1])
# print(dhanish[:5])
# print(dhanish[-1:-5:-1])

# dhanish=(1,2,3,4,56,4,11,12,14,16,17)
# for i in range(len(dhanish)):
#     if dhanish[i] ==(4):
#        dhanish.index(4)
#        print(i)

# #4.count()
# count=(1,2,3,4,5,6,7,4,11,21,4,121,34,4,56)
# print(count.count(4))

# #tuple operators
# #1.concatenation
# tuple1=(1,2,3,4,5,6)
# tuple2=(7,8,9,10,11,12)
# tuple3=tuple1+tuple2
# print(tuple3)

# #2.repetation
# tuple=(21,22,23,24,25,26,27)
# print(tuple*2)

# #membership test
# tuple=(21,22,23,24,25,26)
# print(21 not in tuple)
# print(20 in tuple)
# print(21 in tuple)

# #coding exercise
# '''
# 1.create a tuple:write a program that creates a tuple that containing three elements your name,age and your
# favourite colour.then print the tuple
# '''
# personal_info=(("name","dhanish reddy kethireddy"),("age",24),("favourite colour","red"))
# print(personal_info)

# '''
# 2.acess tuple elements:write a python program that creates a tuple containing the days of the week.then print the 
# third element of the tuple
# '''
# days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
# print(days[2])

# '''
# 3.tuple concatenation:write a pyhton programm that creates two tuples one containg odd numbers 1 to 5 and another 
# containing even numbers 2 to 6, concatenate these two tuples and print the result
# '''
# tuple1=(1,3,5)
# tuple2=(2,4,6)
# print(tuple1+tuple2)

# '''
# 4.tuple unpacking:write a python program that defines a tuple containing the dimensions of a
# rectangle(length*width).then,unpack this tuple into two variables and calculate the area of the rectangle
# '''
# tuple=(23,45)
# length=tuple[0]
# width=tuple[1]
# area_of_a_rectangle=length*width
# print(f'the area of rectangle is {area_of_a_rectangle}')

# '''
# 5.check if an element exists:write a program that checks if a given element exists in a tuple
# '''
# tragedy=(("apple",80),("banana",90),("orange",100))
# print(("apple",80) in tragedy)
# print(('orange',100) in tragedy)
# print(('banana',90) in tragedy)

# '''
# 6.write a python program to generate a bill for a super market purchase.the program should store the items
# and their prices in a list of tuples.it should then iterate over this list to print out each item along with its 
# price .finally calculate and print the total cost of all the items.
# '''
# items=[("Apple",99),("Banana",99),("milk",49)]
# total=0
# print("item    price")
# print("="*13)
# for i,j in items:
#     print(f"{i}    {j}")
#     total+=j
# print("="*13)
# print(f"total  {total}")
# print("="*13)

