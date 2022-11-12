from game_data import data
import ascii
import random
from os import system, name

end_game = False
score = 0

def clear():
    if name == 'nt':
        _ = system('cls')

def get_data():
  return random.choice(data)

def display():
    print(ascii.logo)
    print(f"Compare A: {position_A['name']}, {position_A['description']} from {position_A['country']}.")
    print(ascii.vs)
    print(f"Compare A: {position_B['name']}, {position_B['description']} from {position_B['country']}.")
    
def get_selection(): 
    global user_selection
    global alt_option
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
        user_selection = position_A
        alt_option = position_B
    elif choice == 'B':
        user_selection = position_B
        alt_option = position_A
    else:
        print("Invalid selection!")
        get_selection()     

def compare():
    global position_A
    global position_B
    global end_game
    if user_selection["follower_count"] > alt_option["follower_count"]:
        score += 1
        position_A = user_selection
        position_B = get_data()
    else: 
        end_game = True



position_A = get_data()
position_B = get_data()

while not end_game:
    get_data()
    display()
    end_game = True