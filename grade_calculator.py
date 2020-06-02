math_mark = int(input("Please input your Math mark: "))
chemistry_mark = int(input("Please input your Chemistry mark: "))
physics_mark = int(input("Please input your Physics mark: "))
total_grade = int((math_mark + chemistry_mark + physics_mark)/3)

print("Your total grade is ", total_grade)

if total_grade >= 70:
    print("A")
elif total_grade >= 60:
    print("B")
elif total_grade >= 50:
    print("C")
elif total_grade >= 40:
    print("D")
else:
    print("You failed")