#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # def __init__(self, name="dog"):
    def __init__(self, name="dog", breed="Mastiff"):

        self.name = name
        self.breed = breed

    def get_name (self):
        return self._name
    
    def set_name (self,name):
        if (type(name) == str) and (0 < len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.") 

    def get_breed (self):
        return self._breed
    
    def set_breed (self, breed):
        if (breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
    pass
print("Mastiff" in APPROVED_BREEDS)

# fido = Dog("fido", "brah")
# print(fido.name, fido.breed)


# class Human:
#     species = "Homo sapiens"

#     def __init__(self, age):
#         self.age = age

#     def get_age(self):
#         print("Retrieving age.")
#         return self._age

#     def set_age(self, age):
#         if (type(age) in (int, float)) and (0 <= age <= 120):
#             print(f"Setting age to { age }.")
#             self._age = age

#         else:
#             print("Age must be a number between 0 and 120.")

#     age = property(get_age, set_age)

# bob = Human(56)
# print(bob.age)

# class Person:
#     def __init__(self, age):
#         self.age = age  # Note: We use a leading underscore to indicate this is a "private" attribute.

#     def get_age(self):
#         print("Getting age...")
#         return self._age

#     def set_age(self, age):
#         print("Setting age...")
#         self._age = age

#     age = property(get_age, set_age)

# # Creating an instance of the Person class
# bob = Person(30)
# print(bob.age)

# # Accessing the age property (calls the getter)
# # print(person.age)  # Output: "Getting age..." 30

# # Setting the age property (calls the setter)
# # person.age = 35  # Output: "Setting age..."

# # Accessing the age property again (calls the getter)
# # print(person.age)  # Output: "Getting age..." 35