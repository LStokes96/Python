def zip(string1,string2):
    list1 = list(string1)
    list2 = list(string2)
    i = 0
    while i  < len(list1):
        n = 0
        while n < len(list2):
            list2.insert(n,list1[i])
            i += 1
            n += 2
    return  ''.join(list2)

print(zip("String","Fridge"))
