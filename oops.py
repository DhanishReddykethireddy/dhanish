# #oops class,object and self

# #example.1:
# class customer_info():
#     name='ramu'
#     mobile_number=9898765432
#     item='phone'
#     cost=20000
#     item_2='laptop'
#     cost2=35000
#     item_3='MI tv'
#     cost3=23000
#     def details(self):
#         print(f'customername:{self.name} and mobile number {self.mobile_number}')
#     def product(self):
#         self.details()
#         print(f'the product you have selected {self.item} and the cost is {self.cost}')
#         print(f'the product you have selected {self.item_2} and the cost is {self.cost2}')
#         print(f'the product you have selected {self.item_3} and the cost is {self.cost3}')
#         print(f'the total cost that you have to pay is:{self.cost+self.cost2+self.cost3}')
# bill=customer_info()
# bill.details()
# print(bill.item)
# bill.product()

# #example.2:
# class mobile():
#     brand='vivo'
#     model='x200'
#     ram='12gb'
#     storage='256gb'
#     def device_details(d):
#         print(f'brand:{d.brand},model:{d.model}')
#     def information(i):
#         print(f'ram:{i.ram},storage:{i.storage}')
# phone=mobile()
# print(phone.brand)
# print(phone.ram)
# phone.device_details()
# phone.information()

# #self keyword
# class details():
#     name='dhanish'
#     age = 24
#     height=5.89
#     def info(self):
#         print(f'name:{self.name},age:{self.age}')
#     def info2(self):
#         print(f'the height is {self.height}')
# data=details()
# data.info()
# data.info2()


#__init__ method():

#example1
class bike():
    def __init__(self,brand,model,year,topspeed):
        self.brand=brand
        self.model=model
        self.year=year
        self.topspeed=topspeed
    def buy(self):
        print(f'you are going to buy {self.model} in {self.brand}')
    def details(self):
        print(f'the bike was manufactured in the year {self.year}')
    def speed(self):
        print(f'the topspeed of that bike is {self.topspeed}km/hrs')
    
            
vehicle=bike("bajaj","pulsar150","2021",120)
vehicle.buy()
vehicle.speed()
vehicle.details()
print(vehicle.brand)

vehicle2=bike('hero','xpulse',2024,125)
vehicle2.buy()
vehicle2.speed()
vehicle2.details()

# #exmaple.2:
# class district_info():
#     def __init__(self,district_name,no_of_mandals,no_of_villages,no_of_people):
#         self.district_name=district_name
#         self.no_of_madals=no_of_mandals
#         self.no_of_villages=no_of_villages
#         self.no_of_people=no_of_people
#     def district(self):
#         print(f'the disrict:{self.district_name} has {self.no_of_madals} mandals')
#     def villages(self):
#         print(f'the district:{self.district_name}  has {self.no_of_villages} villages')
#     def people(self):
#         print(f'the district:{self.district_name}  has {self.no_of_people} population')
# place=district_info('kadapa',36,726,'20,60,654')
# place.district()
# place.villages()
# place.people()

# place2=district_info('ananthapur',63,1213,'40,83,315')
# place2.district()
# place2.villages()
# place2.people()

# #task 
# '''
# practice using classes and objects by writing a program  to create a laptop object
# '''
# class lap():
#     def __init__(self,brand_name,model_name,screen_size,version,cost):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.screen_size=screen_size
#         self.version=version
#         self.cost=cost
#     def brand(self,e):
#         print(f'the laptop i bought from {self.brand_name} company and model is {self.model_name} and version is {self.version}',e)
#     def details(self):
#         print(f'the display size of my lap is {self.screen_size}cms and the cost is {self.cost}rs')
# laptop=lap('HP','probook',13.5,13,44000)
# laptop.brand('windows')
# laptop.details()

# laptop2=lap('dell','vostro',14.5,13.5,44000)
# laptop2.brand('inspirion')
# laptop2.details()

