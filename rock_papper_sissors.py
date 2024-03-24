import random 

def game():
    user_score=0
    computer_score=0
    while True:
        choice=int(input("Enter your choice:\n1)play again\n2)view score\n3)terminate\n "))

        if choice==1:   
            uinput=input("Enter your choice rock, papper or scissors: ")
            lst=["rock","papper","scissors"]
            cinput=random.choice(lst)

            if cinput==uinput:
                print()
                print("It's a draw!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print()
                user_score+=1
                computer_score+=1
            
            elif cinput=="papper" and uinput=='scissors' or cinput=="rock" and uinput=='papper' or cinput=="scissors" and uinput=='rock':
                print()
                print("Users's win!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print()
                user_score+=2

            elif uinput=="rock" and cinput=='papper' or uinput=="papper" and cinput=='scissors' or uinput=="scissors" and cinput=='rock':
                print()
                print("Computer's win!!!\n","User's input: ",uinput,"\nComputer's input: ",cinput, sep="")
                print()
                computer_score+=2

        elif choice==2:
            print()
            print("User's score:",user_score)
            print("Computer's score:",computer_score)
            print()

        elif choice==3:
            print("Programme terminates!!!")
            break

        else:
            print("Invalid input!!!")
     
game()