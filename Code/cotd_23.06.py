def scram(numbers,letters):
    num =list(str(numbers))
    let = list(str(letters))
    new_list = let
    i = 1
    for n in range (len(num)):
        new_list.insert(i,num[n])
        i += 2
    return ''.join(new_list)

print(scram(1234,"abcde"))