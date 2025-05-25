# #set
# set={'dhani','sandy',142,}
# print(set)

# #set methods()
# #1.add()
# set_1={12,13,14,15,16,17}
# set.add(143)
# print(set)

# #2.clear()
# set_1={1,2,3,4,5,6,7}
# set_1.clear()
# print(set_1)

# #3.copy()
# set_1={"dhanish",143,"sandy",}
# set_2=set_1.copy()
# print(set_1)

# #4.pop
# dhani={1,2,3,4,5,6,76}
# dhani.pop()
# print(dhani)

# #5.remove()
# sandy={"short",5.8,22}
# sandy.remove('short')
# print(sandy)

# #6.discard()
# sandy={12,13,14,15,16}
# sandy.discard(12)
# sandy.discard(555)
# print(sandy)

# #7.update()
# string={"name","dhanish","age",24}
# info={"good person",5.89, "height"}
# string.update(info)
# print(string)

# #frozen set
# set={1,2,3,4,5,6,7,8}
# set_1=frozenset(set)
# print(set_1)
# print(type(set_1))

# #set operations
# #1.union()
# maths_marks={30,40,50,60,70}
# science_marks={35,45,55,60,70,100}
# print(maths_marks.union(science_marks))
# print(science_marks.union(maths_marks))

# score={140,150,160,170,180}
# score_1={190,200,210,220,287}
# print(score.union(score_1))
# print(score_1.union(score))

# #2.intersection()
# ds={12,13,14,15,16}
# sd={16,14,17,18,19,20,21}
# print(ds.intersection(sd))

# #3.symmetric_difference
# make={12,13,14,15,16,17,18}
# made={12,13,21,22,23,24,25}
# print(make.symmetric_difference(made))

# #4.isdisjoint()
# dhani={1,2,3,4,5}
# sandy={6,7,8,9,10}
# print(dhani.isdisjoint(sandy))

# harish={1,2,3,4,5}
# krish={5,6,7,8,9}
# print(harish.isdisjoint(krish))

# #5.differnce
# set_1={30,31,32,33,34}
# set_2={33,34,35,36,37}
# print(set_1.difference(set_2))
# print(set_2.difference(set_1))

# # 6.issuperset()
# # 7.issubset()
# dhani={21,22,23,24,25}
# sandy={21,22,23,24}
# print(dhani.issuperset(sandy))
# print(sandy.issubset(dhani))
# print(sandy.issuperset(dhani))
# print(dhani.issubset(sandy))

# #coding excercises
# #task1:set intersection
# '''
# write a python code to find and print the union of the following tow sets
# '''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.union(set2))

# #task.2:set union
# '''
# write a python code to find and print the union of the following two sets
# '''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.union(set2))

# #task.3:set difference
# '''
# write a python code to find and print the elements present in set1 but not in set2'''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.difference(set2))

# #task.4:set symmetric differnce
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.symmetric_difference(set2))

# #task.5:membership test
# '''
# write a python code to check if the element 3 is present in the set my_set
# '''
my_set={1,2,3,4,5}
print(3 in my_set)

# # #exercises
# # #exercise.1:set intersection
# '''
# write a python script that finds and print the intersection of two sets
# '''
# set1={41,42,43,44,45}
# set2={44,45,46,47,48}
# print(set1.intersection(set2))

# #exercise.2:set union
# '''
# write a python script that finds and the union of two sets
# '''
# driver1speed={"4okm","50km","60km","70km","80km"}
# driver2speed={"70km","80km","90km","100km","110km"}
# print(driver1speed.union(driver2speed))

# #exercise.3:set difference
# '''write a python script that finds and prints the differnce between two sets'''
# driver1speed={"4okm","50km","60km","70km","80km"}
# driver2speed={"70km","80km","90km","100km","110km"}
# print(driver1speed.difference(driver2speed))
# print(driver2speed.difference(driver1speed))

# #exercise.4:set symmetric difference
# '''write a python script that finds and prints the symmetric difference between two sets'''
# driver1speed={"4okm","50km","60km","70km","80km"}
# driver2speed={"70km","80km","90km","100km","110km"}
# print(driver1speed.difference(driver2speed))
# print(driver2speed.difference(driver1speed))


