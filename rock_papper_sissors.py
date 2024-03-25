import random 

def game():
    user_score=0
    computer_score=0
    while True:
        choice=int(input("\n1)play again\n2)view score\n3)exit\n\nEnter your choice:"))

        if choice==1:   
            while (1):
                uinput=input("\nrock, papper or scissors: ")
                lst=["rock","papper","scissors"]
                if (uinput not in lst):
                    print("invalid input!!!")
                else:
                    break
            cinput=random.choice(lst)

            if cinput==uinput:
                print("\n=======================================================================================")
                print("It's a draw!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print("=======================================================================================")
 
            
            elif cinput=="papper" and uinput=='scissors' or cinput=="rock" and uinput=='papper' or cinput=="scissors" and uinput=='rock':
                print("\n=======================================================================================")
                print("Users's win!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print("=======================================================================================")
                user_score+=2

            elif uinput=="rock" and cinput=='papper' or uinput=="papper" and cinput=='scissors' or uinput=="scissors" and cinput=='rock':
                print("\n=======================================================================================")
                print("Computer's win!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print("=======================================================================================")
                computer_score+=2

        elif choice==2:
            print("\n=======================================================================================")
            print("User's score:",user_score)
            print("Computer's score:",computer_score)
            print("=======================================================================================")

        elif choice==3:
            print("\n=======================================================================================")
            print("User won!" if user_score > computer_score else "Computer won!" if user_score < computer_score else "It's a tie!")
            print("=======================================================================================\n")
            print("Thanks for playing the game!!!")
            break

        else:
            print("Invalid input!!!")
     
game()