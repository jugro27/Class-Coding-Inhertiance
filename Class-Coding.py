class Animal:
    """Animal Class"""
    def __init__(self, name):
        print("Initializing name")
        self.__name = name

    @property
    def name(self):
        print("Getting name")
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Setting name")
        self.__name = new_name

    @name.deleter
    def name(self):
        print("Deleting name")
        del self.__name
    
    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Book:
    """Book Class"""
    def __init__(self, title):
        print("Initializing title")
        self.__title = title

    @property
    def title(self):
        print("Getting title")
        return self.__title

    @title.setter
    def title(self, new_title):
        print("Setting title")
        self.__title = new_title

    @title.deleter
    def title(self):
        print("Deleting title")
        del self.__title

    def __init__(self, ISBN):
        print("Initializing ISBN")
        self.__ISBN = ISBN


    @property
    def ISBN(self):
        print("Getting ISBN")
        return self.__ISBN

    def __init__(self, yearPublished):
        print("Initializing year published")
        self.__yearPublished = yearPublished

    @property
    def yearPublished(self):
        print("Getting year published")
        return self.__yearPublished

    def __init__(self, author):
        print("Initializing author")
        self.__author = author

    @property
    def author(self):
        print("Getting author")
        return self.__author


class Vehicle:
    """Vehicle class"""
    def __init__(self, make):
        print("Initializing make")
        self.__make = make

    @property
    def make(self):
        print("Getting make")
        return self.__make

    def __init__(self, model):
        print("Initializing model")
        self.__model = model

    @property
    def model(self):
        print("Getting model")
        return self.__model

    def __init__(self, year):
        print("Initializing year")
        self.__year = year

    @property
    def year(self):
        print("Getting year")
        return self.__year

    def __init__(self, VIN):
        print("Initializing VIN")
        self.__VIN = VIN

    @property
    def VIN(self):
        print("Getting VIN")
        return self.__VIN

    def __init__(self, licensePlate):
        print("Initializing license plate")
        self.__licensePlate = licensePlate

    @property
    def licensePlate(self):
        print("Getting license plate")
        return self.__licensePlate

    def accelerate(self):
        print("accelerating")

    def brake(self):
        print("braking")
    
    def turn(self):
        print("Turning")

    def reverse(self):
        print("Reversing")

    def radio(self):
        print("Playing radio")

    def airConditioning(self):
        print("Air conditioning on")

    def heat(self):
        print("Heat is on")

    def wipers(self):
        print("Wipers are on")

    def honk(self):
        print("Honking")

    def headLights(self):
        print("Headlights are on")