
def date_fashion(you, date):
    if (you or date >= 8) and (you or date >= 3):
        return 2 
    elif you or date <= 2:
        return 0
    else:
        return 1

print(date_fashion(2,10))
print(date_fashion(5,2))
print(date_fashion(5,5))
