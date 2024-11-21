print("Welcome to the Personality Quiz !")
print("Answer  the following questions to find out your personality type .\n")
score =0
#question 1
print("1. what do you like to do in your free time?")
print("a) go out with friends")
print("b) read books")
print("c) Play video games")
print("d) Exercise")
Choice1 = input("Enter your choice (a,b,c or d):").lower()
if Choice1 == "a":
    score +=1
elif Choice1 == "b":
    score +=2
elif Choice1 =="c":
    score +=3 
elif Choice1 =="d":
    score +=4
else:
    print('invalid choice, moving to the next question .\n ')    
print("\n2. how do you handle tasks or projects ?")
print("a) jump right in and figure it out as I go")
print("b) plan everything out before starting .")
print("c) start with small and build up gradually .")
print("d) leave it")    
Choice2 = input("Enter your choice (a,b,c or d):").lower()

if Choice2 == "a":
    score +=2
elif Choice2 == "b":
    score +=3
elif Choice2 =="c":
    score +=4 
elif Choice2 =="d":
    score +=1
else:
    print('invalid choice, moving to the next question .\n ') 
print("what do you do when you are sad ?")
print("a) I prefer to live alone")
print("b) Try to handle the situation")  
print("c) I write some nobels")
print("d) thinks alot")
Choice3 = input("Enter your choice (a,b,c or d):").lower()

if Choice3 == "a":
    score +=3
elif Choice3 == "b":
    score +=2
elif Choice3 =="c":
    score +=4 
elif Choice3 =="d":
    score +=1
else:
    print('invalid choice, moving to the next question .\n ') 
if score <= 5:
    personality = "Thinker - You love deep conversations and insightful books."
elif 6 <= score <= 8:

    personality = "Social Butterfly - You enjoy being around people and having fun."
elif 9 <= score <= 11:
    personality = "Adventurer - You love trying new things and taking risks!"
else:
    personality = "Leader - You’re bold, confident, and enjoy taking charge."
print(f"\nYour personality type is {personality}")   
print(f"your total score is : {score}")