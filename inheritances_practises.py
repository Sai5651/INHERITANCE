# single inheritance
class Vehicle_Factory:
    def __init__(self,name,age_of_vehicle,price):
        self.name = name
        self.age_of_vehicle = age_of_vehicle
        self.price = price
# intialize and it accesa construvor
class Customer1(Vehicle_Factory):
    def Buying_vehicle(self):
        print('buying the vehicle from vehicle factory')
        bike = 'bajaj'
        age = '2 years'
        price = '25,000'
        print('my requirements the bike should be',bike,'and age will be below',age,'price should be ',price)
        if self.name == bike:
            print('yes we have that bike ')
        if self.age_of_vehicle == age:
            print('yes we have that type of bikes ')
        if self.price == price:
            print('done sir we have ')
        else:
            print('sorry your requirements did not match for us ')

#c = Customer1('bajaj','2 years','25,000')
#c.Buying_vehicle()

'''----------------------------------------------------------------------------------'''
# multiple inheritance
# when one child can aquire the properties and data from two parent class

class Bangalore_cricket_stadium:
    def Bangalore_ground(self):
        self.bground = 'china swamy stadium'
        self.bplace = 'bangalore'
        self.barea_size = '16.51 acres'
        self.bseating_capacity = '40,000'

class Hyderabad_cricket_stadium:
    def __init__(self):
        self.hground = 'Rajiv gandhi cricket stadium'
        self.hplace = 'hyderabad'
        self.harea_size = '16 acres'
        self.hseating_capacity = '55,000'

class Domestic_grounds(Hyderabad_cricket_stadium,Bangalore_cricket_stadium):
    def Ground1(self,name):
        super().Bangalore_ground()
        self.name = name
        print(f'ground name is {self.name}')
        print(f'ground size is {self.harea_size}')
        print(f'ground capacity is {self.bseating_capacity}')

#d = Domestic_grounds()
#d.Ground1('chandu')

'''----------------------------------------------------------------------------------'''
# multi level inheritance
# multi level inheritance is nothing but like line by line any one can acces any one like
# 1-2-3-4 like it will goes like a line it is called multi level inheritance
# child class can access parent class and sub child class can access child class but finaly one sub class ca acces both child and parent class

class Chandu:
    def __init__(self):
        self.cbike = 'R15'
        self.chelemet = 'Steel Bird'
        self.cJacket = 'Rynox'
class Arjun(Chandu):
    def Chandu_property(self,bike,helmet,jacket):
        self.bike = bike
        self.helemet  = helmet
        self.jacket = jacket
        print('my name is arjun ')
        print('my bike is ',self.bike)
        print('iam using ',self.helemet,'helemet')
        print('iam wearing ',self.jacket,'jacket')

class Kishore(Arjun):
    def Arjun_property(self):
        print('my name is kishore ')
        print('my bike is ', self.cbike)
        print('iam using ', self.chelemet, 'helemet')
        print('iam wearing ', self.cJacket, 'jacket')

#k = Kishore()
#k.Chandu_property('bullet','royal enfield','rynox')
#k.Arjun_property()
'''----------------------------------------------------------------------------------'''
# hirarichal inheritance
'''here the hirarical means it is quite opposite to the multiple inheritance 
like one parent and more childs multiple childs can aquire the data and methods from 
one parent class itself '''

class Kritunga:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        print(f'restaurent name is {self.name} and it is located in {self.location}')
    def Veg(self,*items):
        self.veg_items = items
    def Non_veg(self,*nitems):
        self.non_veg = nitems

class Customer_1(Kritunga):
    def Foods_ordering(self):
        super().Veg('panner biriyani','mushroom biriyani','roti panner curry','gobi manchurian','dal tadka','vegitable rise','mushroom rise')
        super().Non_veg('chicken biriyani','mutton biriyani','kushka','egg rise','roti chicken curry','shawarma','butter chicken','chennur dhum biriyani')
        print(f'iam a vegetarian i need this food for lunch  {self.veg_items[0:3:1]}')
        print(f'and my frnd is a non-vegetarian i need this food like {self.non_veg[0:3:1]}')

class Customer_2(Kritunga):
    def Food_ordering(self):
        super().Veg('panner biriyani','mushroom biriyani','roti panner curry','gobi manchurian','dal tadka','vegitable rise','mushroom rise')
        super().Non_veg('chicken biriyani','mutton biriyani','kushka','egg rise','roti chicken curry','shawarma','butter chicken','chennur dhum biriyani')
        print(f'iam a vegetarian i need this food for lunch  {self.veg_items[0:3:1]}')
        print(f'and my frnd is a non-vegetarian i need this food like {self.non_veg[3]}')

#obj = Customer_2('kritunga','bangalore')
#obj.Food_ordering()
#obj1 = Customer_1('imperial','bangalore')
#obj1.Foods_ordering()
'''---------------------------------------------------------------------------------'''
# hybrib inheritance
''' in this inheritance a child can acces from two or more parent classes as well as 
 two or more child classes can access one parent class iike it is a combination of
  hirarichal inheritance and multiple inheritance '''

class Mobile:
    def Sim1(self):
        print('iam having only one sim ')
class Mobile2:
    def Sim2(self):
        print('iam having 2 sims ')
class Mobile3:
    def Sim3(self):
        print('iam having 3 sims ')

class user(Mobile,Mobile2):
    def Users(self):
        print('iam having both sim1 and sim2')


#u = user()
#u.Sim2()
#u.Sim1()
'''--------------------------------------------------------------------------------'''
# these are called the types of inheritance  in oops
# you can use by removing the [# tag]