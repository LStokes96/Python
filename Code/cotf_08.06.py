def three(a):
    part_1 = a*1
    part_2 = a*11
    part_3 = a*111
    part_4 = a*1111
    return part_1 + part_2 + part_3 + part_4

a = int(input("Enter a number: "))
print(three(a))