import sys
import random

ans = True

while ans:
    question=input("Ask the magic 8 ball a question: ")

    answers = random.randint(1,8)

    if question =="":
        sys.exit()

    elif answers == 1:
        print("it is certain")

    elif answers == 2:
        print("Outlook good")
    
    elif answers == 3:
        print("You may rely on it")
    
    elif answers == 4:
        print("ask again later")
    
    elif answers == 5:
        print("Concentrate and ask again")

    elif answers == 6:
        print("Reply hazy, try again")

    elif answers == 7:
        print("My reply in no")

    elif answers == 8:
        print("My source says no")
