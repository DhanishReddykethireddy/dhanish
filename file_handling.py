# file handling
# r mode
# a mode
# w mode

# #r mode ----- read operations in an existing file
# #read()
# file=open("demo.txt",mode='r')
# read_data=file.read()
# print(read_data)
# file.close() 

# #readlines()
# file=open("demo.txt",mode='r') 
# data=file.readline()
# print(data)
# file.close()

# #readlines
# file=open("demo.txt",mode='r')
# read=file.readlines()
# print(read)
# file.close()

# a mode ----open an existing file to write a new text and we can create a new file by using a mode

# #a mode
# #write --- writes a specified string to the file
# file = open("demo.txt",mode='a')
# write_data=file.write('\ni am doing well')
# file.close()

# #a mode
# #write     ---- we can create a new txt file
# file=open("sample.txt",mode='a')
# write_data=file.writelines('this is your family')
# file.close()

# #writelines()----write a list of strings to the file
# names=['dhanish\n','sandhya\n','sandeep\n','krish\n']
# file=open("sample3.txt",mode='a')
# write_data=file.writelines(names)
# file.close()

# #w mode 
# #write ---- writes a specified string to the file but we will loss data
# file=open("sample.txt",mode='w')
# write_data=file.writelines('this is your kingdom\n this is your rule')
# file.close()

# #writelines()----write a list of strings to the file
# names=['dhanish\n','sandhya\n','sandeep\n','krish\n']
# file=open("sample.txt",mode='w')
# write_data=file.writelines(names)
# file.close()

# #write ---- writes a specified string to the file but we will loss data
# file=open("sample1.txt",mode='w')
# write_data=file.writelines('this is your kingdom\n this is your rule')
# file.close()

# #writelines()----write a list of strings to the file
# names=['dhanish\n','sandhya\n','sandeep\n','krish\n']
# file=open("sample2.txt",mode='w')
# write_data=file.writelines(names)
# file.close()


# #w+ mode
# file=open("sample3.txt",mode='w+')
# write_data=file.write("dhanish\nthat is my name")
# print(file.tell())
# file.seek(0)
# read_data=file.read()
# print(read_data)
# file.close()


# #a+ mode
# file=open("demo.txt",mode='a+')
# write_data=file.write('\nmy fav place is hyderabad\nbut i love my village more than this')
# file.seek(0)
# read_data=file.read()
# print(read_data)
# file.close()


# #r+ mode
# file=open("demo.txt",mode='r+')
# write_data=file.write("i dont know how to give mock in interviews\ni need to learn that how i have to perform in interviews\n")
# file.close() 

# file=open("demo.txt",mode='r+')
# read_data=file.readlines()
# print(read_data)
# file.close()


