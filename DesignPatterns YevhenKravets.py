#!/usr/bin/env python
# coding: utf-8

# In[12]:
#Adapter
#I will use adapter design pattern for conecting Integer to Strings

class String:     # Creating String 
    def get(self):
        return "1997"
class Integer:    # Creating integer 
    def get_int(self):
        return 1998

# Creating adapter ,it makes Strings out of Integers

class Adapter(Integer):
    def get(self):
        return str(self.get_int())
# main
def main(obj):
    print ("Result is : " + obj.get())
#start
if __name__ == '__main__':
    obj = Adapter()
    main(obj)


# In[18]:
#Singleton
#Singleton is a generative design pattern that checks that a class has only instance, and provides a global access point to it.
#Singleton allows you to access a single instance of it from any point in the client code 
#Instance creation is done by the principle of delayed initialization
# creating main class with a dictionary that checks for the presence of a singleton and, if it is not present, makes new

class SingletonStartClass(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonStartClass, cls).                __call__(*args, **kwargs)
        return cls._instances[cls]


#This is our singleton which is inherited through the metaclass and some variables

class First_singleton(metaclass=SingletonStartClass):
    def __init__(self):
        self.name = "My Singleton"
        self.value_x = 10
        self.value_y = 100

    def add_x_y(self) -> int:
        return self.value_x+self.value_y

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

#Initialsation and functioning test
if __name__ == "__main__":
    
    my_singleton_1 = First_singleton()
    my_singleton_2 = First_singleton()
    print("Singleton1 name: " + my_singleton_1.get_name())
    my_singleton_1.set_name("Updated Singleton")
    print("Singleton2 name: " + my_singleton_2.get_name())
    print(my_singleton_1)
    print(my_singleton_2)
    print(id(my_singleton_1) == id(my_singleton_2))


# In[17]:


#Facade


#Facade pattern is used here to delegate most of the work to other classes
#I have 4 classes each of which have thier job to do
#Using this design pattern i can put all the logic in one class

class Foundation:
    def foundate(self):
        print("Making foudation")

class Walls:
    def bild_wall(self):
        print("Bilding Walls")

class Roof:
    def install_roof(self):
        print("Installing a roof")

class Dekor:
    def decorate(self):
        print("Decorating inside")

class BuildingFacade:
    def __init__(self):
        self.foundation = Foundation()
        self.walls = Walls()
        self.roof = Roof()

    def build_house(self):
        for i in range(2):
            self.foundation.foundate()

        for i in range(4):
            self.walls.bild_wall()

        for i in range(1):
            self.roof.install_roof()

        print("House is built")

class Facade:
    def __init__(self):
        self.building_facade = BuildingFacade()
        self.dekor = Dekor()

    def start_project(self):
        self.building_facade.build_project()
        for i in range(10):
            self.dekor.decorate()

if __name__ == '__main__':
    facade = BuildingFacade()
    facade.build_house()