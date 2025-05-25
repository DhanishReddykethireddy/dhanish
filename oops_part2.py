# #inheritance
# #1.single inheritance
# class calculation():
#     def __init__(self,number1,number2):
#         self.number1=number1
#         self.number2=number2
#     def add(self):
#         print(f'calculating addition:{self.number1+self.number2}')
#     def mul(self):
#         print(f'calculating multiplication:{self.number1*self.number2}')
#         self.add()
# class calculating(calculation):
#     def sub(self):
#         print(f'calculating substraction:{self.number1-self.number2}')
#         calculating.add(self)
        
# maths=calculating(100,150)
# maths.add()
# maths.mul()
# maths.sub()
# print(maths.number1)


# #example2________single inheritance
# class toys():
#     def __init__(self,toy1,toy2,toy3,child1,child2,child3):
#         self.toy1=toy1
#         self.toy2=toy2
#         self.toy3=toy3
#         self.child1=child1
#         self.child2=child2
#         self.child3=child3
#     def play1(self):
#         print(f'{self.child1} is playing with {self.toy3}')
#         print(f'{self.child2} is crying for {self.toy3}')
#     def play2(self):
#         print(f'{self.child2} is playing with {self.toy2}')
#         print(f'{self.child1} is crying for {self.toy2}')
# class playtime(toys):
#     def play3(self):
#         print(f'{self.child3} is playing with {self.toy1}')
#         print(f'{self.child1} is crying for {self.toy1}')
#     def crying(self):
#         print(f'{self.child1} is happy wiht {self.toy1}')
#         print(f'{self.child2} is happy wiht {self.toy2}')
#         print(f'{self.child3} is happy wiht {self.toy3}')
#         print('care taker solved  all the problems and made the children happy and got some relaxation')
# children=playtime('car','helicopter','cube','anup','sankar','vijay')
# print('toy1 name is ',children.toy1)
# print('toy2 name is ',children.toy2)
# print('toy3 name is ',children.toy3)
# print('child1 name is',children.child1)
# print('child2 name is ',children.child2)
# print('child3 name is ',children.child3)
# children.play1()
# children.play2()
# children.play3()
# children.crying()
        
# #2.multi level inheritnace
# class Family():
#     def __init__(self,grandfather,grandmother,son,sonwife,child,job,place,girl):
#         self.grandfather=grandfather
#         self.grandmother=grandmother
#         self.son=son
#         self.sonwife=sonwife
#         self.child=child
#         self.job=job
#         self.place=place
#         self.girl=girl
#     def basefamily(self):
#         print(f'the base family is {self.grandfather} family')
#         print(f'the male person in base family is {self.grandfather} and his wife is {self.grandmother}')
#         print(f'the son of {self.grandfather} and {self.grandmother} is {self.son}')
# class Family2(Family):
#     def nextgeneration(self):
#         print(f'the  nextfamily of {self.grandfather} family is {self.son} family')
#         print(f'{self.son} is son of {self.grandfather}')
#         print(f'the male person in this family is {self.son} and his wife is {self.sonwife}')
#         print(f'the son of {self.son} and {self.sonwife} is {self.child}')
# class Family3(Family2):
#     def futuregeneration(self):
#         print(f'the next family of {self.son} family is {self.child} family')
#         print(f'{self.child} is son of {self.son}')
#         print(f'{self.child} is completed his studies and getting ready for marriage')
#         print(f'{self.son} is doing job as {self.job} at {self.place}')
#         print(f'finally {self.child} is going to marry {self.girl}')
#         print(f'{self.child} is going to live life happily with {self.girl}')
          
# familydrama=Family3('rangarao','yasodha','bhanu','samantha','varun tej','software engineer','bangloere','sunayana')
# familydrama.basefamily()
# familydrama.nextgeneration()
# familydrama.futuregeneration()


# #3.multiple inheritance()
# class schoolinfo():
#     def __init__(self,school_name,school_location):
#         self.school_name=school_name
#         self.school_location=school_location
#     def school(self):
#         print(f'my schooling was completed in {self.school_name} at {self.school_location}')
        
# class collegeinfo():
#     def __init__(self,college_name,college_location):
#         self.college_name=college_name
#         self.college_location=college_location
#     def college(self):
#         print(f'my intermediate was completed in {self.college_name} collage at {self.college_location}')
        
# class studies(schoolinfo,collegeinfo):
#     def __init__(self,school_name,school_location,college_name,college_location):
#         schoolinfo.__init__(self,school_name,school_location)
#         collegeinfo.__init__(self,college_name,college_location)
#     def education(self):
#         print('these are my educational details')

# study=studies('ZPHS','kadapa','chaithnya','ananthapur')
# study.school()
# study.college()
# study.education()

# #example2.........
# class animal_info():
#     def __init__(self,animal_name,animal_type,living_place):
#         self.animal_name=animal_name
#         self.animal_type=animal_type
#         self.living_place=living_place
#     def animal(self):
#         print(f'the animal name is {self.animal_name} and its type is {self.animal_type} and it lives in {self.living_place}')
        
# class pet_info():
#     def __init__(self,pet_name,pet_type,behaviour):
#         self.pet_name=pet_name
#         self.pet_type=pet_type
#         self.behaviour=behaviour
#     def  pet(self):
#         print(f'the pet name is {self.pet_name},he belongs to {self.pet_type} family,he is {self.behaviour}')
        
# class crop_info:
#     def __init__(self,crop_name,duration,cost):
#         self.crop_name=crop_name
#         self.duration=duration
#         self.cost=cost
#     def crop(self):
#         print(f'the crop in our field is {self.crop_name},the duration of the crop is {self.duration} and the cost of the crop for 1000kg is Rs.{self.cost}')
        
# class overview(animal_info,pet_info,crop_info):
#     def __init__(self, animal_name, animal_type, living_place,pet_name,pet_type,behaviour,crop_name,duration,cost):
#         animal_info.__init__(self,animal_name, animal_type, living_place)
#         pet_info.__init__(self,pet_name,pet_type,behaviour)
#         crop_info.__init__(self,crop_name,duration,cost)
#     def exit(self):
#         print("i am getting exit from the multiline inheritance")

# details_of_everything=overview('cheetah','wild animal','forest','krish','dog','very friendly','banana','8 to 12 months',12000)
# details_of_everything.animal()
# details_of_everything.pet()
# details_of_everything.crop()

# #4.heirarchial inheritance()
# class student():
#     def __init__(self,student1_name,student1marks,student2_name,student2marks):
#         self.student1_name=student1_name
#         self.student1marks=student1marks
#         self.student2_name=student2_name
#         self.student2marks=student2marks
#     def s1(self):
#         print(f'the 1st student name is {self.student1_name} and he got {self.student1marks}')
#     def s2(self):
#         print(f'the 2nd student name is {self.student2_name} and he got {self.student2marks}')

# class marks_of_student1(student):
#     def __init__(self,student1_name,student1_marks,student2_name,student2_marks):
#         student.__init__(self,student1_name,student1_marks,student2_name,student2_marks)
#     def final_info(self):
#         print(f'this is the final progress of {self.student1_name}')
# marks_info=marks_of_student1('ravi','580/600','amar','544/600')
# marks_info.s1()
# marks_info.final_info()

# class marks_of_student2(student):
#     def __init__(self,student1_name,student1_marks,student2_name,student2_marks):
#         student.__init__(self,student1_name,student1_marks,student2_name,student2_marks)
#     def final_info(self):
#         print(f'this is the final progress of {self.student2_name}')
# marks_info=marks_of_student1('ravi','580/600','amar','544/600')
# marks_info.s2()
# marks_info.final_info()

# #inheritance ============================>1.single inheritance
# class atm():
#     def __init__(self,bank_name,location,balance):
#         self.bank_name=bank_name
#         self.location=location
#         self.balance=balance
# class menu(atm):
#     def display_menu(self):
#         print('ATM MENU')
#         print('1.credit')
#         print('2.debit')
#         print('3.balance enquary')
#         print('4.exit') 
#     def choices(self):
#         choice=input('choose your choice from the atm options:')
#         if choice in ['1','2','3','4']:
#             return choice
#         else:
#             print('choose the correct option from the atm options')
#     def credit(self):
#         credit_amount=float(input('enter the creidt amount:'))
#         if credit_amount <=0:
#             print('enter the correct amount')
#         else:
#             self.balance+=credit_amount
#             print(f'Rs{credit_amount} is added to your account successfully')
#     def debit(self):
#         debit_amount=float(input('enter the amount to be debited:'))
#         if debit_amount<=0:
#             print('enter the correct amount')
#         else:
#             if debit_amount > self.balance:
#                 print('insufficient balance in your bank')
#             else:
#                 self.balance-=debit_amount
#                 print(f'Rs{debit_amount} has debited from your account')   
#     def enquary(self):
#         print(f'the balance in your bank acount is {self.balance}')
    
# bank=menu('SBI','PULIVENDULA',500)
# print('-'*50)
# print(f' '*5,"wecome to {bank.bank_name} atm,{bank.location}")
# print(' '*9,'Welcome to the SBI atm services')
# print('-'*50)
# bank.display_menu()
# while True:
#     option=bank.choices()
#     if option=='1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.enquary()
#     elif option == '4':
#         print('-'*30)
#         print('Thank you for using SBI using ATM services')
#         print('Have a nice day')
#         break

# #inheritance=================>2.multi level inheritance
# class atm():
#     def __init__(self,bank_name,location,balance):
#         self.bank_name=bank_name
#         self.location=location
#         self.balance=balance
# class menu(atm):
#     def display_menu(self):
#         print('ATM MENU')
#         print('1.credit')
#         print('2.debit')
#         print('3.balance enquary')
#         print('4.exit') 
#     def choices(self):
#         choice=input('choose your choice from the atm options:')
#         if choice in ['1','2','3','4']:
#             return choice
#         else:
#             print('choose the correct option from the atm options')
# class deposit(menu):
#     def credit(self):
#         credit_amount=float(input('enter the creidt amount:'))
#         if credit_amount <=0:
#             print('enter the correct amount')
#         else:
#             self.balance+=credit_amount
#             print(f'Rs{credit_amount} is added to your account successfully')
#     def debit(self):
#         debit_amount=float(input('enter the amount to be debited:'))
#         if debit_amount<=0:
#             print('enter the correct amount')
#         else:
#             if debit_amount > self.balance:
#                 print('insufficient balance in your bank')
#             else:
#                 self.balance-=debit_amount
#                 print(f'Rs{debit_amount} has debited from your account')   
#     def enquary(self):
#         print(f'the balance in your bank acount is {self.balance}')
    
# bank=deposit('SBI','PULIVENDULA',500)
# print('-'*50)
# print(f' '*5,"wecome to {bank.bank_name} atm,{bank.location}")
# print(' '*9,'Welcome to the SBI atm services')
# print('-'*50)
# bank.display_menu()
# while True:
#     option=bank.choices()
#     if option=='1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.enquary()
#     elif option == '4':
#         print('-'*50)
#         print('Thank you for using SBI using ATM services')
#         print('Have a nice day')
#         break

# #inheritance ============================>3.multiple inheritance()
# class atm():
#     def __init__(self,bank_name,location,balance):
#         self.bank_name=bank_name
#         self.location=location
#         self.balance=balance
# class menu():
#     def display_menu(self):
#         print('ATM MENU')
#         print('1.credit')
#         print('2.debit')
#         print('3.balance enquary')
#         print('4.exit') 
#     def choices(self):
#         choice=input('choose your choice from the atm options:')
#         if choice in ['1','2','3','4']:
#             return choice
#         else:
#             print('choose the correct option from the atm options')
# class deposit():
#     def credit(self):
#         credit_amount=float(input('enter the creidt amount:'))
#         if credit_amount <=0:
#             print('enter the correct amount')
#         else:
#             self.balance+=credit_amount
#             print(f'Rs{credit_amount} is added to your account successfully')
# class withdraw(atm,menu,deposit):
#     def debit(self):
#         debit_amount=float(input('enter the amount to be debited:'))
#         if debit_amount<=0:
#             print('enter the correct amount')
#         else:
#             if debit_amount > self.balance:
#                 print('insufficient balance in your bank')
#             else:
#                 self.balance-=debit_amount
#                 print(f'Rs{debit_amount} has debited from your account')   
#     def enquary(self):
#         print(f'the balance in your bank acount is {self.balance}')
    
# bank=withdraw('SBI','PULIVENDULA',500)
# print('-'*50)
# print(f' '*5,"wecome to {bank.bank_name} atm,{bank.location}")
# print(' '*9,'Welcome to the SBI atm services')
# print('-'*50)
# bank.display_menu()
# while True:
#     option=bank.choices()
#     if option=='1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.enquary()
#     elif option == '4':
#         print('-'*50)
#         print('Thank you for using SBI using ATM services')
#         print('Have a nice day')
#         break

# # inheritance =================>4.heirarchial inheritance
# class atm():
#     def __init__(self,bank_name,location,balance):
#         self.bank_name=bank_name
#         self.location=location
#         self.balance=balance
# class menu():
#     def __init__(self,atm):
#         self.atm=atm
#     def display_menu(self):
#         print('ATM MENU')
#         print('1.credit')
#         print('2.debit')
#         print('3.balance enquary')
#         print('4.exit') 
#     def choices(self):
#         choice=input('choose your choice from the atm options:')
#         if choice in ['1','2','3','4']:
#             return choice
#         else:
#             print('choose the correct option from the atm options')
# class deposit():
#     def __init__(self,atm):
#         self.atm=atm
#     def credit(self):
#         credit_amount=float(input('enter the creidt amount:'))
#         if credit_amount <=0:
#             print('enter the correct amount')
#         else:
#             self.atm.balance+=credit_amount
#             print(f'Rs{credit_amount} is added to your account successfully')
# class withdraw():
#     def __init__(self,atm):
#         self.atm=atm
#     def debit(self):
#         debit_amount=float(input('enter the amount to be debited:'))
#         if debit_amount<=0:
#             print('enter the correct amount')
#         else:
#             if debit_amount > self.atm.balance:
#                 print('insufficient balance in your bank')
#             else:
#                 self.atm.balance-=debit_amount
#                 print(f'Rs{debit_amount} has debited from your account') 
# class balance_enquary():
#     def __init__(self,atm):
#         self.atm=atm  
#     def enquary(self):
#         print(f'the balance in your bank acount is {self.atm.balance}')
    
# ATM=atm('SBI','PULIVENDULA',500)
# print('-'*50)
# print(f' '*5,"wecome to {bank.bank_name} atm,{bank.location}")
# print(' '*9,'Welcome to the SBI atm services')
# print('-'*50)
# bank=menu(atm)
# bank.display_menu()
# while True:
#     option=bank.choices()
#     if option=='1':
#         bankdeposit=deposit(ATM)
#         bankdeposit.credit()
#     elif option == '2':
#         bankwithdrawl=withdraw(ATM)
#         bankwithdrawl.debit()
#     elif option == '3':
#         bankbalance_enquary=balance_enquary(ATM)
#         bankbalance_enquary.enquary()
#     elif option == '4':
#         print('-'*50)
#         print('Thank you for using SBI using ATM services')
#         print('Have a nice day')
#         break

