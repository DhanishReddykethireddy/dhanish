#create a dictionary
details={
    'name':'dhanish',
    'age':24,
    'height':5.89,
    'weight':'74kgs',
    'state':'Andhra pradesh',
    'district':'Y.S.R kadapa',
    'mandal':'lingala',
    'village':'diguvapalli'
}
print(details)
#dictionary methods
#1.clear()
cricket={1:'bat',2:'ball',3:'wickets',4:'stumps',5:'players',6:'empires'}
cricket.clear()
print(cricket)

#2.copy
cricket={1:'bat',2:'ball',3:'wickets',4:'stumps',5:'players',6:'empires'}
game=cricket.copy()
print(f'game={game}')

#3.get()
cricket={1:'bat',2:'ball',3:'wickets',4:'stumps',5:'players',6:'empires'}
print(cricket.get(1))
print(cricket[3])

#4.keys()
pulivendula={'area':'flowers street','area1':'new rtc bus stand','area3':'shilparamam'}
print(pulivendula.keys())

#5.values()
pulivendula={'area':'flowers street','area1':'new rtc bus stand','area3':'shilparamam'}
print(pulivendula.values())

#6.items()
pulivendula={'area':'flowers street','area1':'new rtc bus stand','area3':'shilparamam'}
print(pulivendula.items())

#7.pop()
pulivendula={'area':'flowers street','area1':'new rtc bus stand','area3':'shilparamam'}
kadapa=pulivendula.pop('area1')
print(kadapa)
print(pulivendula)

#8.update()
dict={'city':'hyderabad','ipl team':'SRH','logo':'eagle symbol'}
dict_1={'captian':'pat cummins','hitter':'abhishek sharma','local player':'NKR'}
dict.update(dict_1)
print(dict)

csk={'cap':'dhoni','city':'chennai','local player':'ruturaj'}
csk['local player']='ashwin'
csk['coach']='flemming'
print(csk)

#Task.1:dictionary update
'''
write a pyhton code to add a new key value pair to the following dictionary
'''
my_dict={'name':'pyhton','age':25}
my_dict['city']='west godavari'
print(my_dict)

#Task.2:dictionary acess
'''write a python code to access and print the value associated with the key price in the 
following dictionary'''
product_info={'name':'laptop','brand':'dell','price':1200}
print(product_info['price'])

#Task.3:dictionary removal
'''write a pyhton code to remove key value pair from the following dictionary'''
my_dict={'name':'python','age':30,'city':'rajamundry'}
my_dict.pop('city')
print(my_dict)

#Task.4:dictionary keys
'''write a pyton code to print all the keys present in the following dictionary'''
my_dict={'name':'python','age':30,'city':'rajamundry'}
print(my_dict.keys())

#Task.5:dictonary values
'''write a python code to print all the values present in the following dictionary'''
my_dict={'name':'python','age':25,'city':'tanuku'}
print(my_dict.values())

# #Exercise.1:dictionary update
'''write a python script that updates a dictionary with a new key value pair'''
player_info={'matches':220,'innings played':50,'player type':'all rounder'}
player_info['runs scored']=4400
player_info['wickets taken']=244
print(player_info)

#Exercise.2:dictionary acess
'''write a python script that acesses and prints the values associated with a 
specific key in a dictionary'''
player_info={'matches': 220, 'innings played': 50, 'player type': 'all rounder', 'runs scored': 4400, 'wickets taken': 244}
print(player_info['player type'])

#Exercise.3:dictionary removal
'''write a python script that removes a key value pair from a dictionary'''
player={'matches': 220, 'innings played': 50, 'player type': 'all rounder', 'runs scored': 4400, 'wickets taken': 244}
player.pop('player type')
print(player)

#Exercise.4:dictionary keys
'''write a python script that prints all the keys present in the dictionary'''
info={'matches': 220, 'innings played': 50, 'player type': 'all rounder', 'runs scored': 4400, 'wickets taken': 244}
print(info.keys())

#Exercise.5:dictionary values
'''write a python script that prints all the values present in the dictionary'''
info={'matches': 220, 'innings played': 50, 'player type': 'all rounder', 'runs scored': 4400, 'wickets taken': 244}
print(info.values())


