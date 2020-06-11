def two(number):
    if number == 1:
        return False
    else:
        for x in range(2,number):
            if (number % x == 0):
                return False
        return True

print(two(11))