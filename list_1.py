#1.reverse list
'''
write a python code to reverse the order of elements in the given list my_list.print
the reversed order.'''
my_list=[10,20,30,40,50,11]
print(my_list)
print(my_list[::-1])
my_list.reverse()
print(my_list)

#2.common elements
'''
given two list1 and list2,find and print the common elemnts between them'''
list_1=[1,2,3,4,5]
list_2=[4,5,6,7,8]
list_3=[]
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
print(list_3)

#3.unique elements
'''create a new list unique_list containing only the unique welements from the given list 
given list original_list.print the unique list.'''
original_list=[1,2,2,3,4,4,5]
unique_list=[]
for i in original_list:
    if i not in unique_list:
     unique_list.append(i)
print(unique_list)

#4.remove duplicates
'''
remove duplicate elements from the given list duplicated_list and print the list without
duplicates while preserving the order'''
duplicated_list=[1,2,2,3,4,4,5]
list_after_removal_duplicates=[]
for i in duplicated_list: 
    if i not in list_after_removal_duplicates:
        list_after_removal_duplicates.append(i)
print(duplicated_list)
print(list_after_removal_duplicates)

#5.list concatenation
'''
write a pythonn script that concatenates two list and print results'''
list_1=[1,2,3,4,5]
list_2=["dhani","sandy","python","list"]
list_3=list_1+list_2
print(list_3)

#6. list repetation
'''
write a python script that repeats a list three times and print the result'''
list_1=[1,2,3,4,5]
print(list_1*3)

#7.list removal
'''write a python script that removes the element at even indicates from a list '''
list=[1,2,3,4,5,6,7,8,9]
empty_list=[]
for i in list:
    if i%2!=0:
        empty_list.append(i)
print(empty_list)

#8.list insertionn
'''write a python list that inserts the number 10,11 and 12 at the beginning of alist'''
list=[23,45,67,43,56,12,43,443,456,444]
dhani=[10,11,12]
print(dhani+list)

list=[23,45,67,43,56,12,43,443,456,444]
list.insert(0,10)
list.insert(1,11)
list.insert(2,12)
print(list)

#9.list comprehensions
'''
1.square numbers:create a list of square from 1 to 10'''
print([i**2 for i in range(1,11)])

'''
2.even numbers:generate a list of even numbers from 1 to 20'''
for i in range(1,21):
    if i%2==0:
        print(i)

even_numbers=[i for i in range(1,21) if i%2==0]
print(even_numbers)

'''
3.words_length:given alist of words,create a list containing the lengths of each word'''
words=["apple","banana","cherry","date"]
for i in words:
    if i in words:
        print(len(i))
        
print([len(i) for i in words if i in words])

'''
4.print cubes from 1 to 10 using list comprehension'''
print([i**3 for i in range(1,11)])

'''
5.finding index by using list comprehension'''
dhani=[12,19,45,178,478]
print([dhani.index(i) for i in dhani])