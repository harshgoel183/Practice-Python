#date, name, price = ['december 23,2015', 'bread gloves', 8.51]
#print(name)

def drop_first_last(grades):
    first, *middle, last = grades #*middle will take all the items in the middle
    avg = sum(middle)/len(middle)
    print(avg)
drop_first_last([65,76,44,87,45])
drop_first_last([65,76,44,87,45,55,75,87,24])
