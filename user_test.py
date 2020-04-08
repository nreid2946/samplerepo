class User:
  def __init__(self, full_name, birthday):
      self.name = full_name
      self.birthday = birthday #yyyy.mm.dd format

      name_pieces = full_name.split(" ")
      self.first_name = name_pieces[0]
      self.last_name = name_pieces[-1]

user = User("Dave Bowman", "19720398")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

# user = User("Dave Bowman", "19720398")
#       print(user.full_name)
#       print(user.first_name)
#       print(user.last_name)
#       print(user.birthday)
