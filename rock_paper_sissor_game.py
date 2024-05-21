import random
count=0
def cases(y):
     match y:
        case 1:
                return "scissors"
        case 2:
                return "paper"
        case 3:
                return "rock"
        case _:
                return "none"

choices=["rock","paper","scissors"]
while True :
        random_choice = random.choice(choices)
        user_input=int(input("choose 1)Rock 2)Papper 3)Scissors 4)none"))
        user_choice = cases(user_input)
        if user_choice=="none":
              exit()
        elif (user_choice == "scissors" and random_choice == "rock") or \
       (user_choice == "rock" and random_choice == "paper") or \
       (user_choice == "paper" and random_choice == "scissors"):
               print("you lost")
               count+=1
        else :
               count+=1
               print("you won")
               break
               
print(f'you won in { count} tries')





   

                
                
        

    
            




