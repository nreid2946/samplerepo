import sys
import string

class User:
    pass

user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name)
print(user1.last_name)

first_name = "Arthur"
last_name = "Clarke"
print(first_name)

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

print(first_name, last_name)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

user1.age = 37

user2.favourite_book = "2001: A Space Odyssey"

print(user1.age)

def __init__(self, full_name, birthday):
    self.name = full_name
    self.birthday = birthday #yyyy.mm.dd format

    name_pieces = full_name.split(" ")
    self.first_name = name_pieces[0]
    self.last_name = name_pieces[-1]

user = User("Dave Bowman", "19720398")
print(user.full_name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
