## Group Information

Subclass: M
Group: M02
Members:
- ANTER Henry | 3036727745
- CHAN Elliot Cheuk Yin | 3036737415
- WONG Wing Lok | 3036812368
- GUO Yi Lin | 3036811728

## Game Name: Mineshaft Escape

You are trapped in an abandoned mineshaft, you need to complete a series of puzzles to obtain drill parts. Then, you need to craft a drill and escape the mineshaft!

## Requirements

- Python 3
- No external libraries are used, all libraries used are standard python libraries
- The game must be run in a terminal that contains keyboard input

## Running the Game

Extract the zip file, change directory to M02_ENGG1330_Project, and to run from docker, run the command: docker compose run --rm game

## How to play

- Main Menu
When the game is started, the main menu is the first thing you see, the player can input numbers 1-7, and each number input will lead to a different function. Alternatively, the user can input 'q' to quit.

- Inventory
When '1' is inputted, it opens a different screen which shows the quantity of parts the user has. Pressing enter returns the user to the main menu.

- Crafting
When '2' is inputted, it leads the player to the crafting screen, displaying a crafting recipe for a drill. pressing 'c' will attempt to craft a drill, and a drill is crafted if the player has sufficient materials, otherwise an 'insufficient parts' message will appear.

- Word Guesser
When '3' is inputted, it leads to the first puzzle, word guesser. It plays exactly like "Wordle", the player must guess a randomly generated 5-letter word, hints are shown in the form of letter position and whether the letter is contained in the word. If the player guesses the word, they win and obtain a drill part, otherwise they lose and return to main menu. inputting q as a guess will also result in returning to main menu.

Limitation: The number of possible words is finite, because the words are simply a list of copy-paste of five-letter words found on google. If possible, it would be ideal to connect it to an online library of five-letter words.

- Fog Maze
When '4' is inputted, it leads to the second puzzle, fog maze. The user traverses a maze where the player can only see a 7 by 7 box around the player. The player uses wasd keys to traverse the maze and attempt to find the exit marked 'x'. The maze is randomly generated everytime. You can press 'q' to quit.

Limitation: There is no real losing conditions, such as time constraints or obstacles that make you lose. The only way to exit the maze is to either quit the game or find the exit marked 'x'.

- Block Push
When '5' is inputted, it leads to the third puzzle, block push. A randomly generated map contains a pressure plate/ goal marked 'P', a block marked 'B', and the player marked 'X'. The goal is to push the block on top of the pressure plate. You win if you can successfully push the block onto the pressure plate. Each position can only be stepped on once, so you cannot step on the same position once, so you lose if you have no more possible moves to complete the objective.

Limitation: the block cannot generate on the side of the map, i.e. near the wall. Otherwise it is impossible to push the block to a plate if the plate is at the middle of the map. Therefore in random.choice(), the option for the block being generated on the side is eliminated.

- Minecart
When '6' is inputted, it leads to the final puzzle, minecart. The player starts at START with 8 units of fuel. Each railway connection requires a specific amount of fuel. The player can only travel to stations directly connected to their current location. The player receives 2 bonus fuel units on the first arrival at station B. This bonus can only be collected one time. Before each movement, the game will display the player's current location, remaining fuel, travel history, and available stations. The player must enter a valid input otherwise he/she will be asked to repeat input until the input is valid. The player can only move if they have enough fuel to pay for the selected route. The player wins by reaching DESTINATION. If the player does not have enough fuel to travel to any connected station, the game ends and then the player can choose to restart (r) or quit (q).

Limitation: There is no randomisation in the routes, each time you play the puzzle, the route is set, so the puzzle gets repetitive. Since the puzzle setup is unique, it was hard to find a way to randomise routes and costs as well while ensuring there was a feasible way to win every time.

- Winning condition
After successfully winning each game once, you will be rewarded with all required drill parts. After you have all 4 drill parts, go to craft (input = 2), and press 'c' to craft the drill. With a drill, you can press '7' in the menu. Option '7' will output the winning message, reset inventory and exit the game if the player has a drill, otherwise it will say that the player does not have the drill.

- Save file:
Unless the player wins the game, the amount of drill parts are saved in the inventory text file even after the player closes the game.

## Contributions

- ANTER Henry

1. menu screen
2. Word Guesser puzzle
3. 1/4 demo
4. Readme

- CHAN Elliot Cheuk Yin

1. Fog maze puzzle
2. 1/4 demo
3. Game concept/ theme

- WONG Wing Lok

1. Block Push puzzle
2. 1/4 demo
3. Game flow idea

- GUO Yi Lin

1. Minecart puzzle
2. Video trailer
3. 1/4 demo