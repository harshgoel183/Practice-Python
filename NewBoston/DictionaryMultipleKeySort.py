from operator import itemgetter

users = [
    {'fname': 'harsh', 'lname': 'goel'},
    {'fname': 'tom', 'lname': 'amada'},
    {'fname': 'tom', 'lname': 'huckr'},
    {'fname': 'tom', 'lname': 'duckr'},
    {'fname': 'sand', 'lname': 'gupta'},
    {'fname': 'shany', 'lname': 'agar'},
    {'fname': 'ram', 'lname': 'wilson'},
    {'fname': 'john', 'lname': 'george'},
    {'fname': 'dash', 'lname': 'williams'},
    {'fname': 'tuna', 'lname': 'fish'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('--------------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
