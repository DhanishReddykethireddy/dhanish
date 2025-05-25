#1.upper and lower()
name='dhanish reddy'
print(name.upper())
chinni='SANDHYA'
print(chinni.lower())

#2.find and index
python='this is python programming language'
print(python.find('python'))
print(python.index('python'))

#3.count()
sample="dhanish reddy kethireddy"
print(sample.count('d'))

#4.replace()
sentece='dhanish is a bad boy'
print(sentece.replace('bad','innocent'))

#5.strip(),lstrip() and rstrip()
line=' this is python '
print(line)
print(len(line))
empty=line.strip()
print(empty)
print(len(empty))

line_1='  my name is noob'
print(line_1)
print(len(line_1))
line_2=line_1.lstrip()
print(line_2)
print(len(line_2))

line_4='my play is like pro   '
print(line_4)
print(len(line_4))
line_3=line_4.rstrip()
print(line_3)
print(len(line_3))

#6.startswtih() and endswith()
names=['dhanish','dhanish.in','harish','harish@gmail.com','suresh','ramesh',]
print([i for i in names if i.startswith('d')])
print([i for i in names if i.endswith('sh')])

#7.split()
sentence='this is a string session practice set'
new_sentence=sentence.split(",")
print(new_sentence)

#8.isdigit() and isalpha() and isalnum()
name="dhanish1234"
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())

noun="dhanish"
print(noun.isdigit())
print(noun.isalpha())
print(noun.isalnum())

number='767488'
print(number.isdigit())
print(number.isalpha())
print(number.isalnum())

#9.title() and capitalize()
book_name='brave story of a boy'
print(book_name.capitalize())
print(book_name.title())

#10.join()
dhanish=["he", "is", "trying", "to", "learn", "pyhton"]
dhani=" ".join(dhanish)
print(dhani)

#coding exercise
'''
1.you are given a string sentence. print the charater at even indices
'''
sentence='python is amazing'
print(len(sentence))
print(sentence[0:17:2])

'''
2.you have given a string s replace all spaces in the string with underscores(_) and print
the modified string'''
s="pyhton is fun and powerfull"
modified_string=s.replace(" ","_")
print(modified_string)

'''
3.you are given a string s.check the string contai only digits
'''
s='1234'
print(s.isdigit())

'''
4.you are given a string s print the string in reverse order
'''
s='pyhton is amazing'
print(len(s))
print(s[-1:-18:-1])

'''
5.you are given a string s.captalize the first letter of each word in the string and print the 
modified string '''
s='python programming is fun'
d=s.title()
print(d)





