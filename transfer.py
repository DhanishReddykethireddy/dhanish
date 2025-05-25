#1.using break in while loop and for loop
'''
1.write a python program that takes a list of numbers as input numbers=[25,30,20,40,15,25] 
and print sum of numbers.however,if the sum exceeds 100,stop adding numbers 
and print"sum exceeded100"'''
sum=0
numbers=[25,30,20,40,15,25]
for i in numbers:
    if sum+i>100:
        print(f'the  sum is {sum} and sum will excedeed 100')
        break
    sum+=i
#using while loop
while True:
    sum=0
    numbers=[25,30,20,40,15,25]
    for i in numbers:
        if sum+i>100:
            print(f'the sum is {sum} will exceeds 100')
            break
        sum+=i
    break

#2.using coontinue in a for loop
'''
write a python program that uses a loop to iterate  through numbers from 1 to 600.
print only the odd numbers,skipping the even ones using the continue statement
'''
num_1=int(input('enter number_1:'))
num_2=int(input('enter number_2:'))
for i in range(num_1,num_2):
    if i%2==0:
        continue
    else:
     print(i)
        
for d in range(1,600,2):
    print(d)

#3.using a pass in cinditional statements
'''
write a python program that checks if a number even or odd.if the number is even,print(even),
if odd,do nothing (use the pass statemnet)
'''
number=int(input('enter a number:'))
if number%2==0:
    print(f'the number is {number} even')
    pass

#4.combining the transfer statements:
'''
write a python program that iterates through a list of words.if the word is "break",exit the 
loop using the break statement.if the word is "skip", skip the rest of the code for the 
current iteration using the continue statement.for any other word print the word
'''
list=['bottle','pass','cricket','continue','ball','break','dhoni','skip',]
for word in list:
    if word=="break":
        break
    elif word == "continue":
            continue
    print(word)
    
cricket_legends=['dhoni','sachin','virat','tim david','dravid','sourav gangully','rohith','rishabh']
for players in cricket_legends:
    if players =='tim david':
        continue
    elif players=='sourav gangully':
        break
    print(players)