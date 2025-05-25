#indexing and slicing
list=[1,2,2.4,5.6,"dhanish","sandy","krish"]
print(list[0])#indexing
print(list[4:6])#slicing
print(list[::-1])#slicing
print(list[4:])#slicing
print(list[:6])#slicing

#list methods
#1.append()
dhanish=[12,13,14,15,16,17,18]
dhanish.append('dhanisandy')
print(dhanish)

#2.extend()
dhanish=[1,2,3,4,5,6,7]
dhanish.extend(['dhanish',143,'sandhya'])
print(dhanish)

#3.copy
dhanish=[1,2,3,4,5,6,7]
sandhya=dhanish.copy()
print(sandhya)

#4.clear()
dhanish=[1,2,3,4,5,6,7]
dhanish.clear()
print(dhanish)

#5.count()
dhanish=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
print(dhanish.count(1))
print(dhanish.count(55))

#6.index
name=['dhanish','sandhya','krish','saraswathi','ramchandra reddy','harish']
print(name.index('krish'))

list=[1,23,44,67,89,45,44,89,34,44,56,57,44]
for i in range(len(list)):
    if list[i]==(44):
        print(i)
        
#list comprehension
print([dhani for dhani in range(len([1,23,44,67,89,45,44,89,34,44,56,57,44])) if list[i]==(44)])
        
#finding index for multiple repeated elements
dhanish=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
for i in range(len(dhanish)):
    if dhanish[i] in(1,55):
        print(i)
print(dhanish[10])

#7.insert
dhanish=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
dhanish.insert(5,'dsuniverse')
dhanish.insert(6,'harish')
print(dhanish)

#8.remove()
dhanish=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
dhanish.remove(4)
print(dhanish)

#removing multiple elments
dhanish2=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
sandhya=[]
for i in dhanish2:
    if i!=(55):
        sandhya.append(i)
print(sandhya)
#list comprehension
print([sandy for sandy in [1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1] if sandy!=55])

#9.pop()
dhanish9=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
dhanish9.pop(0)
print(dhanish9)

#10.reverse()
dhanish4=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
dhanish4.reverse()
print(dhanish4)

11.sort()
dhanish1=[1,2,3,4,55,1,6,7,8,9,55,101,55,1,98,104,143,55,1]
print(dhanish1[5])
dhanish1.sort()
print(dhanish1)
dhanish1.sort(reverse=True)
print(dhanish1)

#lenght function
list=[22,23,24,25,26,78,'dhansih','krish','dhoni','csk','thala for a reason']
print(len(list))
print(list[5])