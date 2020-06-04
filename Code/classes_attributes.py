class Student: 
    def __init__(self, name, age, test):
        self.name = name
        self.age = age
        self.test = test
    _class = "Student"



j_test = int(int(int(input("James Test Score 1: ")) + int(input("James test score 2: ")) + int(input("James test score 3: "))) / 3 )
s_test = int(int(int(input("Sams Test Score 1: ")) + int(input("Sams test score 2: ")) + int(input("Sams test score 3: "))) / 3 )
f_test = int(int(int(input("Freds Test Score 1: ")) + int(input("Freds test score 2: ")) + int(input("Freds test score 3: "))) / 3 )


James = Student("James", "25", j_test)
Sam = Student("Sam", "13", s_test)
Fred = Student("Fred", "45", f_test)


total_scores = getattr(James,"test") + getattr(Sam, "test")
print(total_scores)