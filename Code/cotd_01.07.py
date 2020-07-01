def oddSquare(odd_list):
    for x in range (len(odd_list)):
        if odd_list[x] % 2 == 0:
            odd_list[x] = odd_list[x]
        else:
            odd_list[x] = odd_list[x] * odd_list[x]
    return odd_list

print(oddSquare([1,2,3,4,5,6,7,8,9]))