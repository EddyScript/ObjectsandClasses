#Basics
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.greeting_count = 0

    def addfriends(self,name):
        self.friends = []
        self.friends.append(name)
        print(self.friends)
        self.greeting_count += 1
    def num_friends(self):
        print(len(self.friends),self.greeting_count)
    def __repr__(self):
        return "{0},{1},{2}".format(self.name, self.email, self.phone)#_repr_

sonny = Person("Sonny","sonny@hotmail.com","123-456-7890")
jordan = Person("jordan","jordan@aol.com","098-765-4321")

def greet():
     print ("Hello, I am " + sonny.name + "!")
greet()

def greet():
     print ("Hello, I am " + jordan.name + "!")
greet()

#Make your own class
class Vehicle:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make 
        self.year = year 
    def print_info(self):#Add a method
        print(car.model,car.make,car.year)#Add a method
           
car = Vehicle("Tesla,","Model 3,",",2018")

#sonny.friends.append(jordan)<---add instance var
#jordan.friends.append(sonny)<--- add instance var

#s1 = len(sonny.friends)<--- number of friends
#print(s1)
#j1 = len(jordan.friends)<--- number of friends
#print(j1)

jordan.addfriends(sonny)
jordan.num_friends()
