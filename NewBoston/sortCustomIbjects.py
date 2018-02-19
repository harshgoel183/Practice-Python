from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):#string represtion of object
        return self.name +":"+ str(self.user_id)

users = [
    User('bucky',11),
    User('harsh',33),
    User('ram',63),
    User('tom',7),
    User('jerry',43)
]

for user in users:
    print(user)
print('-----------------')
for user in sorted(users, key=attrgetter('name')):
    print(user)
print('-----------------')
for user in sorted(users, key=attrgetter('user_id')):
    print(user)

