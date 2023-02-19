# ex_1_wild_cat_zoo_encapsulation
Create a class called Person. Upon initialization, it should receive a name and an age. Name mangle the name and the age attributes (should not be accessed outside the class). Create two instance methods called get_name and get_age to return the values of the private attributes.

Test Code

person = Person("George", 32)
print(person.get_name())
print(person.get_age())

Output
George
32
