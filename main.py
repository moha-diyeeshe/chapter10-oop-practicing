class Pet():
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # The following methods are mutators for the
    # class's data attributes
    def set_name(self,name):
        self.__name = name
    def set_animaltype(self,animal_type):
        self.__animal_type = animal_type
    def set_age(self,age):
        self.__age = age
    # attribute methods for accessing

    def get_name(self):
        return  self.__name
    def get_animaltype(self):
        return  self.__animal_type
    def get_age(self):
        return  self.__age

while True:

    name = input("Enter the name of your pet: ")
    if name.strip() and not name.isdigit():# Check if the name is non-empty (ignoring leading/trailing spaces)
        break
    else:
        print("Invalid name. Please provide a non-empty name.")

while True:
    animal_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    if animal_type.strip() and not animal_type.isdigit():  # Check if the animal type is non-empty (ignoring leading/trailing spaces)
        break
    else:
        print("Invalid animal type. Please provide a non-empty type.")

while True:
    age = input("Enter the age of your pet: ")
    if age.isdigit() and int(age) >= 0:  # Check if the age is a non-negative integer
        break
    else:
         print("Invalid age. Please provide a non-negative integer.")

my_pet = Pet(name,animal_type, int(age))

print("information of the pet is: ")
print("Name: ",my_pet.get_name())
print("Animal Type is: ",my_pet.get_animaltype())
print("age is : ",my_pet.get_age())