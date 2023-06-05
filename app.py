# Importing the input_handler module
import input_handler
# Importing the random module
import random
# Intial value of health points for user and computer health points respectively
user_hp=100
comp_hp=100
# Getting user's attack and defence inputs respectively 
user_attack=input_handler.user_Attack_input()
user_defence=input_handler.user_defence_input()
 # Generating a random attack value for the computer
comp_attack=random.randint(0,100)
#  Created a function to determine the computer's attack
def comp_Attack(comp_attack):
        # Return 'punch' if comp_attack is less than or equal to 50
        if(comp_attack<=50):
            return 'punch'
        else:
        # Return 'kick' if comp_attack is greater than 50
            return 'kick'
#Assign a new variable and get the computer's attack value
comp_attack_return=comp_Attack(comp_attack)
#Created a function to determine the computer's defence value low or high based on a random generated value
def comp_defence_input(comp_hp):
    comp_defence=random.randint(0,100)
    if(comp_defence<=50):
       #Return 'low' if comp_defence is less than or equal to 50
      return 'low'
    else:
      # Return 'high' if comp_defence is greater than 50
     return 'high' 

comp_defence=comp_defence_input(comp_hp)  

def comp_game(comp_hp,user_attack,comp_defence):
        # If user attacks with punch and computer defends with high
        if(user_attack=='punch'  and comp_defence=='high'):
        # If user attacks with punch and computer defends with low
            comp_hp-=10
            return comp_hp
         # If user attacks with punch and computer defends with low
        elif(user_attack=='punch'and comp_defence=='low'): 
            comp_hp-=10
            return comp_hp
        # If user attacks with kick and computer defends with high
        elif(user_attack=='kick' and comp_defence=='high'):
            comp_hp-=10
            return comp_hp 
        # If user attacks with kick and computer defends with low       
        elif(user_attack=='kick' and comp_defence=='low'):
            comp_hp-=10
            return comp_hp #returning the new health value for computer 
        else:
           return comp_hp  #return the orginal value of the health value for computer
# created a Function to calculate the user's health points after an attack from 
# the computer and based on a condition reduce by10
def user_game(user_hp,user_defence,comp_attack_return):
        # If computer attacks with punch and user defends with high
        if(comp_attack_return=='punch' and user_defence=='high'): 
            user_hp-=10
            return user_hp
        # If computer attacks with punch and user defends with low
        elif(comp_attack_return=='punch' and user_defence=='low'):  
            user_hp-=10
            return user_hp
         # If computer attacks with kick and user defends with high
        elif(comp_attack_return=='kick' and user_defence=='high'):  
            user_hp-=10
            return user_hp
        # If computer attacks with kick and user defends with low
        elif(comp_attack_return=='kick' and user_defence=='low'):  
            user_hp-=10
            #returning the new health value for user
            return user_hp
        else:
             #return the orginal value of the health value for user
             return user_hp

# Updating user's health points
user_hp=user_game(user_hp,user_defence,comp_attack_return)
# Updating computers health  points
comp_hp=comp_game(comp_hp,user_attack,comp_defence)

# Created function that handles the  main game  loop  for getting a new value from user and computer till we get a Winner.
def main_game(user_hp,comp_hp):
    while(user_hp>0 or comp_hp>0):
        # asking new attack input from the user
        new_ua=input_handler.user_Attack_input()
        # asking new defence input from the user
        new_ud=input_handler.user_defence_input()
        # Getting new attack value for the computer
        new_ca= comp_Attack(comp_attack) 
        # Getting new defence value for the computer
        new_cd =comp_defence_input(comp_hp)
         # Updating user's health points
        new_user_hp=user_game(user_hp,new_ud,new_ca)
        user_hp=new_user_hp
        # Updating computer's health points
        new_comp_hp=comp_game(comp_hp,new_ua,new_cd)
        comp_hp=new_comp_hp
         # Printing user's health points
        print("===================================")
        print("user health point",user_hp)
        # Printing computer's health points
        print("computer health point",comp_hp)
        print("===================================")
        if(new_user_hp==0):
             # Return message if the user's health points reach 0
            return ('You lost!!')
        elif(new_comp_hp==0):
            # Return message if the computer's health points reach 0
            return('you won!!')

# Starting the main game loop
main_game_result=main_game(user_hp,comp_hp) 

#Printing the result of the Game
print(main_game_result)







