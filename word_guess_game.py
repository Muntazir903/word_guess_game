import time,main,crud
from prettytable import PrettyTable

def set_counter(timer):
    for sec in range(timer): 
        print(f"Time left: {timer}sec ",end="\r")
        time.sleep(1) 
        timer-=1  
         
    print("\nTimes up!")

def show_tables():
    table = PrettyTable() 
    table.field_names = [f"Column{num}" for num in range(1,5)] 
    
    table.add_rows([
                ["a","b","c","d"],["e","f","g","h"],
                ["i","j","k","l"],["m","n","o","p"],
                ["q","r","s","t"],["u",'v',"w","x"],
                ["y","z","",""]      
                ])
    
    print(table)  
    
    my_dict= {    
        1 : ["a","e","i","m","q","u","y"],
        2 : ["b","f","j","n","r","v","z"],
        3 : ["c","g","k","o","s","w"],
        4 : ["d","h","l","p","t","x"]   
    }
    
    return my_dict

def get_valid_input(column_range,prompt):
        while True:
            try:
                user_tell = int(input(prompt))
                if user_tell in column_range:
                    return user_tell
                else:
                    print("Invaild column number!")                    
            except ValueError:
                print("Invaild input\nEnter a valid integer!")

def display_user_table(my_dict,user_tells):
    global table2
    table2 = PrettyTable()
    if not user_tells:
        return table2
    
    max_columns = max(len(my_dict[tell]) for tell in user_tells)
                
    for tell in user_tells:
        while len(my_dict[tell]) < max_columns:
            my_dict[tell].append("")
        table2.add_row(my_dict[tell])   

    table2.field_names = [f"Column{num}" for num in range(1,max_columns + 1)]   
    
    print(table2)
    return table2
        
def play_game(): 
      
    print("\n🌟 Welcome to the World of Imagination! 🌟\n")
    print("🕵️ Guess a word in Ten seconds ⏳")
    print("Your time starts now!\n")
    
    set_counter(3)
        
    user_guess = int(input("How many letters your word has: "))

    letter_map= show_tables()
    
    valid_columns = sorted(letter_map.keys())
    user_column = [get_valid_input(valid_columns, f"Alphabet {i+1} from which column? ") for i in range(user_guess)]

    display_user_table(letter_map,user_column)
    
    guessed_word = []
    for alph in range(user_guess):
        user_tell = get_valid_input(valid_columns, f"Alphabet {alph+1} from which column: ")
        guessed_word.append(table2._rows[alph][user_tell - 1])  
                            
    print(f"You guess: {''.join(guessed_word)}🎯")      
 
    
play_game()
        
while True:
    play_again = str(input("Do you want to play again? (y/n) : ")).lower().strip()
    
    if play_again=="y" or play_again=="yes":
        play_game()
    else:
        print()
        print("😊Thanks for playing my game 😊")
        break 







# def play_game():
#     print("\n🌟 Welcome to the World of Imagination! 🌟\n")
#     print("🕵️ Guess a word in Ten seconds ⏳")
#     print("Your time starts now!\n")

#     timer = 10
#     for sec in range(timer): 
#         print(f"Time left: {timer}sec ",end="\r")
#         time.sleep(1) 
#         timer-=1


#     print("\nTimes up!")  
            
#     user_guess = int(input("How many letters your word has: "))

#     table = PrettyTable() 
#     table.field_names = [f"Column{num}" for num in range(1,5)] 
#     table.add_rows([
#                 ["a","b","c","d"],["e","f","g","h"],
#                 ["i","j","k","l"],["m","n","o","p"],
#                 ["q","r","s","t"],["u",'v',"w","x"],
#                 ["y","z","",""]      
#                 ])
#     print(table) 
#     print()
    
#     my_dict= {    
#         1 : ["a","e","i","m","q","u","y"],
#         2 : ["b","f","j","n","r","v","z"],
#         3 : ["c","g","k","o","s","w"],
#         4 : ["d","h","l","p","t","x"]   
#     }

#     table2 = PrettyTable()
#     user_tells = []
#     for alph in range(user_guess):
#         while True:
#             try:
#                 user_tell = int(input(f"Alphabet {alph+1} from which column: "))
#                 if user_tell in my_dict:
#                     user_tells.append(user_tell)
#                     break
#                 else:
#                     print("Invaild column number!")                    
#             except ValueError:
#                 print("Enter a valid integer!")

#     max_columns = max(len(my_dict[tell]) for tell in user_tells)
                
#     for tell in user_tells:
#         while len(my_dict[tell]) < max_columns:
#             my_dict[tell].append("")
#         table2.add_row(my_dict[tell])   

#     table2.field_names = [f"Column{num}" for num in range(1,max_columns + 1)]
#     print()
#     print(table2)      
#     print()
    
#     guessed_word = []
#     for alph in range(user_guess):
#         while True:
#             try:
#                 user_tell = int(input(f"Alphabet {alph+1} from which column: "))
#                 if 1<=user_tell<=max_columns: 
#                     guessed_word.append(table2._rows[alph][user_tell - 1])
#                     break
#                 else:
#                     print("Invaild column number!")   
#             except ValueError:
#                 print("Enter a valid integer!")
                        
#     print()    
#     print(f"You guess: {''.join(guessed_word)}🎯")     
#     print()
    
# play_game()

# while True:
#     play_again = str(input("Do you want to play again? (y/n) : ")).lower().strip()
    
#     if play_again=="y" or play_again=="yes":
#         play_game()
#     else:
#         print()
#         print("😊Thanks for playing my game 😊")
#         break    
    
    

