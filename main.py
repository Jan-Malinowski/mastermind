import random
from colorama import Fore

colors = ["red", "orange", "yellow", "blue", "green", "purple", "white", "black"]
numbers = ["0", "1", "2", "3", "4", "5", "6"]
code = []
error = False
player_code = []
expert = False

# mastermind color
def color_main():
    tries = 0
    code = []
    text = []

    # generating random code
    for i in range(4):
        test = random.choice(colors)
        code.append(test)
    # game with 10 tries. First getting and check input then check if expert mode is on finally print hints
    while tries != 10:
        error = False
        player_input = input(Fore.WHITE + "Please type the code: ")
        player_code = player_input.split()
        if len(player_code) > 4:
            print(Fore.BLUE + "Error! Code is too long!")
            tries -= 1
            error = True
            
        elif len(player_code) < 4:
            print(Fore.BLUE + "Error! Code is too short!")
            tries -= 1
            error = True

        elif error == False:
            for a in range(4):
                if player_code[a] not in colors:
                    print(Fore.BLUE + "Error! Wrong color!")
                    tries -= 1
                    error = True
                    break
                    

        if tries != 9 and error == False:
            text = []
            for i in range(4):
                if(expert == False):
                    if player_code == code:
                        print(Fore.GREEN + "X X X X")
                        print(Fore.GREEN + f"\nYou win!!! Finished in {tries+1} tries!\n" + f"The code was {code}")
                        new_round()
                    elif player_code[i] == code[i]:
                        print(Fore.GREEN + "X", end = ' ')
                        continue
                    elif player_code[i] in code:
                        print(Fore.RED + "O", end = ' ')
                        continue
                    else:
                        print(Fore.WHITE + "_", end = ' ')
                        continue
                else:
                    if player_code == code:
                        print(Fore.GREEN + "X X X X")
                        print(Fore.GREEN + f"\nYou win!!! Finished in {tries+1} tries!\n" + f"The code was {code}")
                        new_round()
                    elif player_code[i] == code[i]:
                        text.append(Fore.GREEN + "X ")
                        continue
                    elif player_code[i] in code:
                        text.append(Fore.RED + "O ")
                        continue
                    else:
                        text.append(Fore.WHITE + "_ ")
                        continue
            if(expert == True):        
                random.shuffle(text)
                for a in range(4):
                    print(text[a], end="")
                print("")    
                    

        print("\n")
        if tries == 9:
            print(Fore.RED + "Game Over!")
            print(Fore.RED + f"The code is {code}")
            new_round()
        tries += 1

# mastermind numbers
def number_main():
    tries = 0
    code = []
    text = []

    #generating random code
    for i in range(4):
        test = random.choice(numbers)
        code.append(test)

    # game with 10 tries. First getting and check input then check if expert mode is on finally print hints
    while tries != 10:
        error = False
        player_input = input(Fore.WHITE + "Please type the code: ")
        player_code = list(player_input)
        res = []
        y = len(player_code)
        x = 0
        # mod input from 1234 to ['1', '2', '3', '4'] or from 1 2 3 4 to ['1', '2', '3', '4']
        while x<y:
            if player_code[x] != " ":
                res.append(player_code[x])
            x+=1
        player_code = res

        if len(player_code) > 4:
            print(Fore.BLUE + "Error! Code is too long!")
            tries -= 1
            error = True
            
        elif len(player_code) < 4:
            print(Fore.BLUE + "Error! Code is too short!")
            tries -= 1
            error = True

        elif error == False:
            for a in range(4):
                if player_code[a] not in numbers:
                    print(Fore.BLUE + "Error! Wrong number!")
                    tries -= 1
                    error = True
                    break
                    

        if tries != 9 and error == False:
            text = []
            for i in range(4):
                if(expert == False):
                    if player_code == code:
                        print(Fore.GREEN + "X X X X")
                        print(Fore.GREEN + f"\nYou win!!! Finished in {tries+1} tries!\n" + f"The code was {code}")
                        new_round()
                    elif player_code[i] == code[i]:
                        print(Fore.GREEN + "X", end = ' ')
                        continue
                    elif player_code[i] in code:
                        print(Fore.RED + "O", end = ' ')
                        continue
                    else:
                        print(Fore.WHITE + "_", end = ' ')
                        continue
                else:
                    if player_code == code:
                        print(Fore.GREEN + "X X X X")
                        print(Fore.GREEN + f"\nYou win!!! Finished in {tries+1} tries!\n" + f"The code was {code}")
                        new_round()
                    elif player_code[i] == code[i]:
                        text.append(Fore.GREEN + "X ")
                        continue
                    elif player_code[i] in code:
                        text.append(Fore.RED + "O ")
                        continue
                    else:
                        text.append(Fore.WHITE + "_ ")
                        continue

            if(expert == True):        
                random.shuffle(text)
                for a in range(4):
                    print(text[a], end="")
            print("")
               
        print("")
        if tries == 9:
            print(Fore.RED + "Game Over!")
            print(Fore.RED + f"The code is {code}")
            new_round()
        tries += 1

# asking for new round after finish last round
def new_round():
    print("")
    reset_inp = input(Fore.WHITE + "Next round? y/n: ")
    if reset_inp.lower() == 'y':
        chose_mode()
    else: 
        exit()

# Chosing mode 
def chose_mode():
    global expert
    inp = input(Fore.WHITE + "Please chose mode color or number? c/n: ")

    if inp.lower() == 'c':
        level_inp = input("Expert? y/n: ")
        if level_inp.lower() == "y":
            expert = True
            print(Fore.BLUE + "Starting...\nYou can use this colors: red orange yellow blue green purple white black\n\n")
            color_main()
        elif level_inp.lower() == "n":
            expert = False
            print(Fore.BLUE + "Starting...\nYou can use this colors: red orange yellow blue green purple white black\n\n")
            color_main()
        else:
            print(Fore.BLUE + "Error\n")
            chose_mode
            
    elif inp.lower() == 'n':
        level_inp = input("Expert? y/n: ")
        if level_inp.lower() == "y":
            expert = True
            print(Fore.BLUE + "Starting...\nYou can use this numbers: 0 1 2 3 4 5 6\n\n")
            number_main()
        elif level_inp.lower() == "n":
            expert = False
            print(Fore.BLUE + "Starting...\nYou can use this numbers: 0 1 2 3 4 5 6\n\n")
            number_main()
        else:
            print(Fore.BLUE + "Error\n")
            chose_mode
    else:
        print(Fore.BLUE + "Error\n")
        chose_mode

# starting game
print(Fore.WHITE + "Mastermind\nLoading...\n")
chose_mode()
