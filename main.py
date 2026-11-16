import random
import os
import sys
import time

#allows ANSI code to work on Windows
if os.name == "nt":
    os.system("")

#refreshes the screen before every output to ensure boundary is kept
def clear_screen():
    if sys.stdout.isatty():
        print("\033[2J\033[H\033[3J", end="", flush=True)
    else:
        os.system("cls" if os.name == "nt" else "clear")

#similar to clear_screen(), used for wordle only
def clear_line():
    print("\033[1A\033[2K\r", end="", flush=True)

#instead of having to input and press enter, it just reads which key is pressed
def get_key():
    try:                     
        import msvcrt
        return msvcrt.getwch()
    except ImportError:
        import termios, tty                
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

#this is the main menu of the game
def menu_screen() -> list[str]:
    return [
        "You wake up at the bottom of an abandoned mineshaft.",
        "The only way out is to craft a drill and dig your way up.",
        "You need to collect 1 of each drill part by completing various puzzles.",
        "",
        "  1. Check Inventory",
        "  2. Crafting",
        "  3. Word Guesser",
        "  4. Fog Maze",
        "  5. Block Push",
        "  6. Minecart",
        "  7. Escape?",
        "",
        "Press 1-7 to choose, q to quit"
    ]

#option 1, it outputs the inventory text file in lines
def inventory_screen():
    with open("MineshaftEscape_inventory.txt", "r") as f:
        print("Your inventory:")
        for line in f:
            print(line)

#after a game completion, the inventory text file is reset
def reset_inventory():
    with open("MineshaftEscape_inventory.txt", "w") as f:
        f.write("Drill engine parts: 0\n")
        f.write("Drill head parts: 0\n")
        f.write("Drill body parts: 0\n")
        f.write("Fuel tank parts: 0\n")
        f.write("Complete drill amount: 0\n")

#this is the screen for crafting a drill
def crafting_screen():
    print("Drill Recipe:\n",
        "x1 Drill engine parts\n",
        "x1 Drill head parts\n",
        "x1 Drill body parts\n",
        "x1 Fuel tank parts\n",
        "\n",
        "Attempt to craft? Press c, otherwise press b to go back to the menu"
            )

#this is the actual drill crafting function
def crafting() -> bool:
    #puts inventory into a dict
    inventory = {}
    with open("MineshaftEscape_inventory.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            item, count = line.strip().split(": ")
            inventory[item] = int(count)

    #checks if have enough of each part
    needed_items = ["Drill engine parts", "Drill head parts", "Drill body parts", "Fuel tank parts"]
    for item in needed_items:
        if inventory.get(item, 0) < 1:
            print("You do not have enough items to craft the drill.")
            return False

    #if enough parts, then drill is crafted
    for part in needed_items:
        inventory[part] -= 1
    inventory["Complete drill amount"] = inventory.get("Complete drill amount", 0) + 1

    #puts updated quantities back into inventory text file
    with open("MineshaftEscape_inventory.txt", "w") as f:
        for item, count in inventory.items():
            f.write(f"{item}: {count}\n")
    
    print("You have successfully crafted a drill! You can now escape the mineshaft!")
    return True

#this is the winning condition, which is "drill is crafted"
def game_cleared() -> bool:
    inventory = {}
    with open("MineshaftEscape_inventory.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            item, count = line.strip().split(": ")
            inventory[item] = int(count)
    
    if inventory.get("Complete drill amount", 0) >= 1:
        return True
    else:
        return False

#when a game is completed, the specified part is written into inventory text file
def part_addition(part_name: str):
    inventory = {}
    with open("MineshaftEscape_inventory.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            item, count = line.strip().split(": ")
            inventory[item] = int(count)
    
    inventory[part_name] = inventory.get(part_name, 0) + 1

    with open("MineshaftEscape_inventory.txt", "w") as f:
        for item, count in inventory.items():
            f.write(f"{item}: {count}\n")
    
    print(f"You have successfully obtained {part_name} (1)!")

#this is puzzle 1, the whole game is in one function
def word_guesser_screen() -> bool:
    clear_screen()
    #screen of the game
    print("WELCOME TO WORD GUESSER")
    print("YOU WILL HAVE 6 TRIES TO GUESS THE WORD AND THE WORD WILL ALWAYS BE 5 LETTERS")
    print("HERE ARE THE RULES:")
    print("IF THE LETTER IS IN THE WORD AND IS IN THE CORRECT POSITION\nTHE LETTER WILL APPEAR IN CAPITAL LETTERS.\nIF THE LETTER IS IN THE WORD\nBUT IS IN THE WRONG POSITION\nTHE LETTER WILL APPEAR IN LOWERCASE.\nIF THE LETTER IS NOT IN THE WORD\nTHE LETTER WILL NOT APPEAR.")
    print("Enter q to quit the puzzle")
    print("=============================================================================")

    #random word obtained
    LIST = ['ABUSE', 'ADULT', 'AGENT', 'ANGER', 'APPLE', 'AWARD', 'BASIS', 'BEACH', 'BIRTH', 'BLOCK', 'BLOOD', 'BOARD', 'BRAIN', 'BREAD', 'BREAK', 'BROWN', 'BUYER', 'CAUSE', 'CHAIN', 'CHAIR', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CLAIM', 'CLASS', 'CLOCK', 'COACH', 'COAST', 'COURT', 'COVER', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CYCLE', 'DANCE', 'DEATH', 'DEPTH', 'DOUBT', 'DRAFT', 'DRAMA', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'EARTH', 'ENEMY', 'ENTRY', 'ERROR', 'EVENT', 'FAITH', 'FAULT', 'FIELD', 'FIGHT', 'FINAL', 'FLOOR', 'FOCUS', 'FORCE', 'FRAME', 'FRONT', 'FRUIT', 'GLASS', 'GRANT', 'GRASS', 'GREEN', 'GROUP', 'GUIDE', 'HEART',  'HORSE', 'HOTEL', 'HOUSE', 'IMAGE', 'INDEX', 'INPUT', 'ISSUE', 'JAPAN', 'JONES', 'JUDGE', 'KNIFE',  'LAYER', 'LEVEL','LIGHT', 'LIMIT', 'LUNCH', 'MAJOR', 'MARCH', 'MATCH', 'METAL', 'MODEL', 'MONEY', 'MONTH', 'MOTOR', 'MOUTH', 'MUSIC', 'NIGHT', 'NOISE', 'NORTH', 'NOVEL', 'NURSE', 'OFFER', 'ORDER', 'OTHER', 'OWNER', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIZE', 'PROOF', 'QUEEN', 'RADIO', 'RANGE', 'RATIO', 'REPLY', 'RIGHT', 'RIVER', 'ROUND', 'ROUTE', 'RUGBY', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SHAPE', 'SHARE', 'SHEEP', 'SHEET', 'SHIFT', 'SHIRT', 'SHOCK', 'SIGHT',  'SKILL', 'SLEEP', 'SMILE', 'SMITH', 'SMOKE', 'SOUND', 'SOUTH', 'SPACE', 'SPEED', 'SPITE', 'SPORT', 'SQUAD', 'STAFF', 'STAGE', 'START', 'STATE', 'STEAM', 'STEEL', 'STOCK', 'STONE', 'STORE', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'TABLE', 'TASTE',  'THEME', 'THING', 'TITLE', 'TOTAL', 'TOUCH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREND', 'TRIAL', 'TRUST', 'TRUTH', 'UNCLE', 'UNION', 'UNITY', 'VALUE', 'VIDEO', 'VISIT', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHILE', 'WHITE', 'WHOLE', 'WOMAN', 'WORLD', 'YOUTH']
    ANSWER = random.choices(LIST)
    ANSWER = ANSWER[0]
    ROUNDS = 6
    available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    available_list = list(available_letters)

    #
    for round in range(ROUNDS):
        print("round:",round+1)
        guess = str(input("Enter your guess: "))

        #allows user to quit the game
        if guess.lower() == 'q':
            print("You quit the game")
            time.sleep(1)
            return False
        
        clear_line()
        clear_line()
        result = ""
        if len(guess) == len(ANSWER):
            if guess.upper() == ANSWER.upper():
                print(ANSWER)
                print("YOU WIN")
                time.sleep(1)
                return True

            for index in range(len(guess)):

                if guess[index].upper() == ANSWER[index]:
                    result += guess[index].upper()

                character_set = set(ANSWER)

                if guess[index].upper() in character_set and guess[index].upper() != ANSWER[index]:
                    result += guess[index].lower()

                if guess[index].upper() not in character_set:
                    result += '_'
                    if guess[index].upper() in available_list:
                        available_list.remove(guess[index].upper())

            #letters not in the word is removed
            available_letters = ""
            for letter in available_list:
                available_letters += letter

            print(f"Round {round+1}:", result, "| Available letters:", available_letters)

        else:
            print("that is not a",len(ANSWER),"letter word")
    else:
        print("The answer was",ANSWER)
        print("YOU LOSE")
        time.sleep(1)
        return False

#2nd puzzle screen, fog maze
def fog_maze() -> bool:
    clear_screen()
    WIDTH = 37
    HEIGHT = 14

    #a random maze is generated using randomised DFS
    def generate_maze(w, h):
        grid = [['#' for _ in range(w)] for _ in range(h)]
        stack = [(1, 1)]
        grid[1][1] = '.'
        
        while stack:
            cx, cy = stack[-1]
            neighbors = []
            for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
                nx, ny = cx + dx, cy + dy
                if 0 < nx < w - 1 and 0 < ny < h - 1 and grid[ny][nx] == '#':
                    neighbors.append((nx, ny, dx, dy))
                    
            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                grid[cy + dy // 2][cx + dx // 2] = '.'
                grid[ny][nx] = '.'
                stack.append((nx, ny))
            else:
                stack.pop()
                
        grid[1][1] = '.'
        grid[h - 2][w - 2] = 'X'
        return grid

    #clears the terminal and draws visible portion of the maze, contains UI
    def display(grid, px, py, steps, message):
        clear_screen()
    
        print(f" LABYRINTH | Steps: {steps} | Status: {message}")
        print("+" + "-" * (WIDTH * 2 + 1) + "+")
    
        for y in range(HEIGHT):
            row_str = "| "
            for x in range(WIDTH):
                dist_x = abs(x - px)
                dist_y = abs(y - py)
            
                # Fog of war logic: only draw within 3 steps
                if x == px and y == py:
                    row_str += "@ "
                elif dist_x <= 3 and dist_y <= 3:
                    row_str += f"{grid[y][x]} "
                else:
                    row_str += "  "
                
            row_str += "|"
            print(row_str)
        
        print("+" + "-" * (WIDTH * 2 + 1) + "+")
        print(" Controls: [W] Up | [A] Left | [S] Down | [D] Right | [Q] Quit")

    #main game loop that manages state and player input
    def main_maze():
        grid = generate_maze(WIDTH, HEIGHT)
        px, py = 1, 1
        steps = 0
        won = False
        message = "Find the exit (X)! Torch radius: 3 steps."

        while True:
            display(grid, px, py, steps, message)
        
            if won:
                return won

            try:
                cmd = get_key().strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                return False

            if not cmd:
                continue

            char = cmd[0]
            if char == 'q':
                print("Exiting game")
                time.sleep(1)
                return False

        
            # Determines movement direction
            dx, dy = 0, 0
            if char == 'w': dy = -1
            elif char == 's': dy = 1
            elif char == 'a': dx = -1
            elif char == 'd': dx = 1
            else:
                continue # Invalid input, just refresh the screen

            # Calculates new position
            nx, ny = px + dx, py + dy
        
            # Checks collision and update state
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if grid[ny][nx] != '#':
                    px, py = nx, ny
                    steps += 1
                
                    if grid[ny][nx] == 'X':
                        won = True
                        message = f"VICTORY! Escaped in {steps} steps!"
                    else:
                        message = "Stepping through the dark..."
                else:
                    message = "Ouch! A solid stone wall."
            else:
                message = "You hit the cave boundary."


    return main_maze()

#3rd puzzle screen
def block_push() -> bool:

    #checks for possible moves
    def possible_moves():
        for d in (-8, 8, -1, 1):
            target = separated_map[person + d]
            if target == '#':
                return True
            if target == 'B' and separated_map[person + 2 * d] != '.':
                return True
        return False

    #initial screen
    clear_screen()
    print("You have to push the block onto the pressure plates puzzle")
    print("person cannot stand on the plate")
    print("b is block, p is plate, X is the person")
    print("w for going forward, a for left, s for back, d for right")
    print("input your movement in a string, such as wdswasdwsa")
    print("you have two chances of inputting your movement")
    print("walking into a wall makes no changes")
    print("pushing the block against the wall makes no changes")
    print("'#' represent road, '.' is wall that block the way")
    print("you cannot step on road you stepped on")
    print("press q to quit the game")
    input("Press Enter to start the puzzle...")
    clear_screen()

    #randomises positions and map
    map='.'*7+'n'+('.'+'#'*5+'.n')*5+'.'*7
    separated_map=[i for i in map]
    indices=[i*8+value for i in range(5) for value in range(9,14)]
    plate=random.choice(indices)
    indices.remove(plate)
    separated_map[plate]='P'
    person=random.choice(indices)
    indices.remove(person)
    separated_map[person]='X'
    side=[9,10,11,12,13,17,21,25,29,33,37,41,42,43,44,45]
    for i in side:
        if int(i) in indices:
            indices.remove(int(i))
    block=random.choice(indices)
    indices.remove(block)
    separated_map[block]='B'
    map=''.join(separated_map)
    newmap=map.replace('n','\n')
    print(newmap)
    while 'P' in separated_map:
        if not possible_moves():
            print('you lost!')
            return False
        
        action = get_key()

        #all actions wasd
        if action=='w':
            if separated_map[person-8]=='P':
                print('The person cannot stand on the plate!')
            if separated_map[person-8]=='B' and separated_map[person-16]!='.':
                separated_map[person-8]='X'
                separated_map[person-16]='B'
                separated_map[person]='.'
                person-=8
                block-=8
            if separated_map[person-8]=='#':
                separated_map[person-8]='X'
                separated_map[person]='.'
                person-=8
        if action=='s':
            if separated_map[person+8]=='P':
                print('The person cannot stand on the plate!')
            if separated_map[person+8]=='B' and separated_map[person+16]!='.':
                separated_map[person+8]='X'
                separated_map[person+16]='B'
                separated_map[person]='.'
                person+=8
                block+=8
            if separated_map[person+8]=='#':
                separated_map[person+8]='X'
                separated_map[person]='.'
                person+=8
        if action=='a':
            if separated_map[person-1]=='P':
                print('The person cannot stand on the plate!')
            if separated_map[person-1]=='B' and separated_map[person-2]!='.':
                separated_map[person-1]='X'
                separated_map[person-2]='B'
                separated_map[person]='.'
                person-=1
                block-=1
            if separated_map[person-1]=='#':
                separated_map[person-1]='X'
                separated_map[person]='.'
                person-=1
        if action=='d':
            if separated_map[person+1]=='P':
                print('The person cannot stand on the plate!')
            if separated_map[person+1]=='B' and separated_map[person+2]!='.':
                separated_map[person+1]='X'
                separated_map[person+2]='B'
                separated_map[person]='.'
                person+=1
                block+=1
            if separated_map[person+1]=='#':
                separated_map[person+1]='X'
                separated_map[person]='.'
                person+=1
        if action=='q':
            print('You quit the game')
            time.sleep(1)
            return False
        clear_screen()
        print(''.join(separated_map).replace('n','\n'))
        if  'P' in separated_map and not possible_moves():
            print('you lost!')
            return False
    print('you won!')
    return True

#4th puzzle, managing fuel
def minecart_screen() -> bool:
    clear_screen()
    #introduction of the puzzle to player
    def display_introduction():
        print("You arrived at an abandoned transportation hub, where you find a minecart.")
        print("You need to take the minecart to the destination in order to get the drill.")
        print("You have originally 8 units of fuel, and there are 2 extra fuel units available at the station B.")
        print("You need to input your routes, calculate fuel requirements, and optimize your travel.")
        print("Let's get started!")
        input("Please Press Enter to continue")

    #show the map to player, unfortunately no random generation
    def display_map():
        print("there is the railway map of the underground railway routes.")
        print("in each route, 'A <--x--> B' indicates that the route between station A and station B requires x units of fuel.")
        print("""
            underground railway routes
        ----------------------------------
            START <--2--> A 
            START <--3--> B
    
            A <--2--> C
            A <--5--> D
    
            B <--2--> C
    
            C <--2--> D
            C <--5--> DESTINATION
    
            D <--2--> DESTINATION
        ----------------------------------
        Extra Fuel Station: B 
        Bonus Fuel: 2 units
        Available only on first arrival.
        ==================================""")
        input("Please Press Enter to continue")

    #show the current status to player
    def display_status():
        print(f"Current location:{current_location}")
        print(f"Current fuel:{fuel}")
        print(f"Travel history:{'->'.join(history)}")
        print(f"Bonus fuel used:{bonus_get}")

    #provide options to travel
    def display_options():
        print("You can choose to travel to the following stations, R to restart, or Q to quit:")
        print("""
        ==================================
                available stations:
        ==================================
              """)
        print()
        for key,value in railway_map[current_location].items():
            print(f"{key} (cost {value} fuels)")

    #allows user to restart
    def restart():
        nonlocal current_location, fuel, history, bonus_get
        current_location = "START"
        fuel = 8
        history = ["START"]
        bonus_get = False
        print("Game has been restarted. You are back at the START station with 8 units of fuel.")
        time.sleep(1)

    #general input function
    def get_answer():
        answer=input("Please input your next station, press R to restart, or Q to quit:").strip().upper()
        while answer not in railway_map[current_location] and answer != "R" and answer != "Q":
            clear_screen()
            print("Invalid station. Please choose a valid station from the available options.")
            display_options()
            answer=input("Please input your next station, press R to restart, or Q to quit:").strip().upper()
        return answer

    #action for minecraft movement
    def move_minecart(answer):
        nonlocal current_location,fuel,history
        if fuel>=railway_map[current_location][answer]:
            fuel-=railway_map[current_location][answer]
            current_location=answer
            history.append(answer)
            bonus_fuel()
        else:
            print("Not enough fuel to move to the selected station. Please choose again.")
            display_options()
            answer = get_answer()
            if answer == "R":
                restart()
            elif answer == "Q":
                return "Q"
            else:
                return move_minecart(answer)

    #when station B, bonus fuel rewarded
    def bonus_fuel():
        nonlocal fuel,bonus_get
        if current_location=="B" and bonus_get==False:
            fuel+=2
            bonus_get=True
            print("You have successfully gotten bonus fuel of 2 units!!!")
            time.sleep(1)

    #checks if game is cleared or not
    def check_game():
        if current_location=="DESTINATION":
            print("Congratulations! You have reached the destination and obtained the drill!")
            print(f"Your travel history: {'->'.join(history)}")
            return (True, True)
        else:
            found=False
            for key,value in railway_map[current_location].items():
                if fuel>=value:
                    found=True
        if found==False:
            print("You do not have enough fuel for any available route. Game over.")
            print(f"Your travel history: {'->'.join(history)}")
            return (True, False)
        return (False, False)
    

    #map in the form of a dictionary
    railway_map={
        "START":{"A":2, "B":3},
        "A":{"START":2, "C":2, "D":5},
        "B":{"START":3, "C":2},
        "C":{"A":2, "B":2, "D":2, "DESTINATION":5},
        "D":{"A":5, "C":2, "DESTINATION":2},
        "DESTINATION":{"C":5, "D":2}
    }
    current_location="START"
    fuel=8
    history=["START"]
    bonus_get=False

    #main game of minecraft fuel management
    display_introduction()
    clear_screen()
    display_map()
    clear_screen()
    success = check_game()
    while success[0]==False:
        clear_screen()
        display_status()
        display_options()
        answer = get_answer()
        if answer == "R":
            restart()
        elif answer == "Q":
            return False
        elif move_minecart(answer) == "Q":
            return False
        success = check_game()
    
    if success[1]==True:
        return True
    else:
        return False

#the actual main game for Mineshaft Escape
if __name__ == "__main__":
    game_running = True
    while game_running:
        clear_screen()
        for line in menu_screen():
            print(line)
        choice = get_key().strip()
        #all choices lead to a different function in the main menu, use if conditions for all
        if choice == '1': #inventory
            clear_screen()
            inventory_screen()
            input("Press Enter to return to the menu...")
        elif choice == '2': #crafting
            clear_screen()
            crafting_screen()
            craft_choice = get_key().strip().lower()
            if craft_choice == 'c':
                crafting()
                input("Press Enter to return to the menu...")
            elif craft_choice == 'b':
                continue
        elif choice == '3': #word guesser
            if word_guesser_screen():
                part_addition("Drill engine parts")
            input("Press Enter to return to the menu...")
        elif choice == '4': #fog maze
            if fog_maze():
                part_addition("Drill head parts")
            input("Press Enter to return to the menu...")
        elif choice == '5': #block push
            if block_push():
                part_addition("Drill body parts")
            input("Press Enter to return to the menu...")
        elif choice == '6': #fuel management
            if minecart_screen():
                part_addition("Fuel tank parts")
            input("Press Enter to return to the menu...")
        elif choice == '7': #escaping
            if game_cleared():
                reset_inventory()
                print("You have successfully escaped the mineshaft! Thanks for playing!")
                game_running = False
            else:
                print("You have not yet crafted the drill to escape.")
        elif choice.lower() == 'q': #to quit the game
            clear_screen()
            print("Exiting game, thanks for playing!")
            game_running = False