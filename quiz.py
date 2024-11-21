#functions 
def quiz_game():
    print("Welcome to the quiz game !")
    score =0 
    #question 1
    print("\n 1. what is the Capital of France ?")
    print("\nA.Berlin\nB. Paris \nC.Madrid \nD.Rome")
    answer = input("your answer").upper()
    if answer =="B":
        print("Correct !")
    else:
        print("Incorrect . the correct answer is B. paris")    

    #question 2
    print("\n What is the result of 3(2*4+8) ?")
    print("A. 6 \nB.34 \nC.48\nD.40")   
    answer = input("your answer").upper()
    if answer =="C":
          print("Correct!")
          score += 1
    else:
         print("Incorrect. The correct answer is C. 48.")  
    print("\n3. Who wrote 'Harry Potter'?")
    print("A. J.R.R. Tolkien\nB. J.K. Rowling\nC. Stephen King\nD. George R.R. Martin")
    answer = input("Your answer: ").upper()
    if answer == "B":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is B. J.K. Rowling.")
    print(f"\nYour final score is: {score}/3")
    if score == 3:  
              print("Congratulations! You got all answers correct!")
    elif score == 2:
        print("Great job! You scored 2 out of 3.")
    elif score == 1:
        print("Good effort! You scored 1 out of 3.")
    else:
        print("Better luck next time!")

quiz_game()     