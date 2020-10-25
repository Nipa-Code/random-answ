# Import the modules
import sys
import random
import time

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1, 16)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print("It is certain")
    
    elif answers == 2:
        print("Outlook good")
    
    elif answers == 3:
        print("You may rely on it")
    
    elif answers == 4:
        print("Ask again later")
    
    elif answers == 5:
        print("Concentrate and ask again")
    
    elif answers == 6:
        print("Reply hazy, try again")
    
    elif answers == 7:
        print("My reply is no")
    
    elif answers == 8:
        print("My sources say no")

    elif answers == 9:
        print("I really don't care")
    
    elif answers == 10:
        print("There is not just one right answer")
    elif answers == 11:
        print("why you need to know?")
    elif answers == 12:
        print("imagine that, there is NO answer for you :D")
    elif answers == 13:
        print("The way you ask, is wrong")
    elif answers == 14:
        print("too hard question...")
        time.sleep(2)
        print("NOW I KNOW")
        time.sleep(2)
        print("I WILL..")
        time.sleep(2)
        print("...QUIT" )
        time.sleep(2)
        break
    elif answers == 15:
        print("Veeeeeeery guud kysymyhys.   :D ")
    elif answers == 16:
        print("w \n e \n  l \n   l \n    p")