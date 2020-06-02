def isbn(digits):
    digit_list = list(map(int, str(digits)))
    print(digit_list)

isbn = [9,7,8,0,3,0,6,4,0,6,1,5]

even = sum(isbn[::2]) * 3
odd = sum(isbn[1::2])

total = even + odd
last_digit = 10-(total/10)
print(int(last_digit))

print(even)
print(odd)
isbn(12345)