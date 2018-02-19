def add_numbers(*args):#* means n no of arguments
    total = 0
    for a in args:
        total += a
    print(total)
add_numbers(3)
add_numbers(4,3,5,2)

