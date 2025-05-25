#4.polymorphism
#5.encapsulation
#6.data abstraction

#4.poymorphism
#implenting same thing in different forms it is of 2 types
#1.overloading ------->1.operator overloading  2.method overloading
#2.method overriding

#1.operator over loading
my_age=44
my_daughter_age=20
print(my_age+my_daughter_age)  #here we are getting addition

his_name='dhanish'
her_name='sandhya'
print(his_name+her_name)   #here we are getting string concatination

#example2
class prepare():
    def done(self):
        print(23+23+24)
    def did(self):
        print('dhanish'+'krish')
obj=prepare()
obj.done()
obj.did()

#2.method overloading
#====>method name should be name
#====>arguements should be different in the terms of length or in the terms of type of arguements
class addition():
    def add(self,a=None,b=None,c=None):
        print(a,b,c)
hen=addition()
hen.add(22,44,55)
hen.add(22,44)
hen.add(44)
hen.add()
hen.add('dhanish','harish','krish')
hen.add('dhanish','harish')
hen.add('dhanish')    
hen.add()

#example.2
class physics():
    def chapter(self,chapter_1=None,chapter_2=None,chapter_3=None):
        print(chapter_1,chapter_2,chapter_3)
subject=physics()
subject.chapter('thermodynamics','law of motion','newton laws')
subject.chapter('thermodynamics','law of motion')
subject.chapter('thermodynamics')
subject.chapter()
subject.chapter(223,456,897)
subject.chapter(223,456)
subject.chapter(223)
subject.chapter()

#2.method overriding
#=====> method should be same and arguements should be also same
class overcome():
    def gen_1(self,a):
        print(f'gen_1 has earned {a} money in his life time,this is base class')
class income(overcome):
    def gen_1(self,a):
        print(f'gen_1 also earned {a} money in his life time,this is derived class')
source=income()
source.gen_1('25 lakhs')   

#example.2
class sign():
    def signature(self,a=None):
        print('this is base class,i got signature from the greatest person',a)     
class autograph(sign):
    def signature(self,a=None):
        print('this is derived class,i got signature from the greatest person',a)  
person=autograph() 
person.signature('MS.DHONI')

#super()
#==>it is used to acess the methods and attributes from base when they are same methods in an class
class overcome():
    def gen_1(self,a):
        print(f'gen_1 has earned {a} money in his life time,this is base class')
class income(overcome):
    def gen_1(self,a):
        print(f'gen_1 also earned {a} money in his life time,this is derived class')
        super().gen_1('50 lakhs')
source=income()
source.gen_1('25 lakhs')  

#example.2
class sign():
    def signature(self,a=None):
        print('this is base class,i got signature from the greatest person',a)     
class autograph(sign):
    def signature(self,a=None):
        print('this is derived class,i got signature from the greatest person',a) 
        super().signature('kane williamson') 
person=autograph() 
person.signature('MS.DHONI') 
  
  
#5.encapsulation
#==>it is a mechanism of wrapping data(variables) and the code acting on the data(methods)together as a single unit.
#it has diff acess modifiers it will provide security to data
#1.public--->accessible to outside
#2.protect---->accesible to derived classes it is declared by using single underscore(_)
#3.private------>not accesible to outside it is declared by using double underscore(__)

#1.public
class public():
    def __init__(self,amount=None,savings=None):
        self.amount=amount
        self.savings=savings
class salary(public):
    def paid(self):
        print('the salary of the person is',self.amount)
class earnings(public):
    def earned(self):
        print("my savings is",self.savings)
obj=salary(25000)
obj. paid()  
obj1=earnings(25000,15000)
obj1.earned()


#protect
class protect():
    def __init__(self,accountnumber=None,amount=None):
        self._accountnumber=accountnumber
        self._amount=amount
class bank(protect):
    def banker(self):
        print('my bank account number is',self._accountnumber)
class money(protect):
    def rupees(self):
        print('the balance amount in my bank is',self._amount)
atm=bank('76742233110','4,44,400')
atm.banker()
cash=money('234567897654','7,77,700')
cash.rupees()

#3.private
class private():
    def __init__(self,name,age,password):
        self._name=name
        self._age=age
        self.__password=password
    def personal(self):
        print('the password of my account is',self.__password)
class details(private):
    def naam(self):
        print('my name is',self._name)
class details2(details):
    def old(self):
        print('your age is',self._age)
                
king=private('daniel','25','7674')
king.personal()
queen=details2('dhoni',44,'7674')
queen.naam()
queen.old()
        

'''
6.data abstraction
-->hiding the implementation and showing only essential part
1.abstract class:
            class which contains abstract methods is called abstract class..
2.abstract method:
           the method which is having only declaration but not defination(hiding the implementation)
--->class which do not have abstract method is called concrete class
--->object cannot be create for abstract class.
--->object can create only for concrete classes.
---->to create abstract classes in python you can use the abc(Abstract Base Classes)module
'''

from abc import ABC,abstractmethod
class company(ABC):
    @abstractmethod
    def model(self):
        pass
class bajaj(company):
    def model(self):
        print("the successful modell in bajaj for 125 and 150 cc is PULSAR")
    def topspeed(self,a,b):
        print(f'the top speed of pulsar125 is {a}kmph and  pulsar150 is {b}kmph')
    def mileage(self,a,b):
        print(f'the mileage of pulsar125 is {a}km per litre and the pulsar150  is {b}km per litre')
class hero(company):
    def model(self):
        print("the successful moedl in hero for 125  is xtreme and 150 cc is achiever")
    def topspeed(self,a,b):
        print(f'the top speed of extreme is {a}kmph and the achiever top speed is {b}kmph')
    def mileage(self,a,b):
        print(f'the mileage of xtreme is {a}km per litre and for achiever is {b}km per litre')
               
bike=bajaj()
bike.model()
bike.topspeed(105,120)
bike.mileage(55,40)

bike2=hero()
bike2.model()
bike2.topspeed(100,110)
bike2.mileage(66,50)

from abc import ABC,abstractmethod
class fruits(ABC):
    @abstractmethod
    def name(self):
        pass
class fruit1(fruits):
    def name(self):
        print('the fruit name is Apple')
    def taste(self):
        print('the taste of the apple is tart')
    def cost(self,a):
        print(f'the cost of the apple is {a} per kg')
class fruit2(fruits):
    def name(self):
        print('the fruit name is pomegranate')
    def taste(self):
        print('the taste of the pomogranate is slight tangy')
    def cost(self,a):
        print(f'the cost of the pomegranate is {a} per kg')
class fruit3(fruits):
    def name(self):
        print('the fruit name is orange')
    def taste(self):
        print('the taste of the orange is sweet and slight tart')
    def cost(self,a):
        print(f'the cost of the orange is {a} per kg')
        
obj=fruit1()
obj.name()
obj.taste()
obj.cost(250)

obj=fruit2()
obj.name()
obj.taste()
obj.cost(300)

obj=fruit3()
obj.name()
obj.taste()
obj.cost(150)
