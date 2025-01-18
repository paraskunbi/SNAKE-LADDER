Snake and Ladder Game
A classic Snake and Ladder game implemented in Python with a Graphical User Interface (GUI) using Tkinter. 
Players can take turns rolling the dice, moving their pieces, and encountering snakes or ladders until someone reaches the 100th square to win the game.

Features
Interactive GUI: Players add themselves, roll the dice, and see their positions update.
Turn-based Gameplay: Automatically switches turns between players.
Snakes and Ladders Logic: Automatically adjusts the player’s position based on predefined snake and ladder positions.
Win Detection: Notifies when a player wins and ends the game.

Game Rules
Players take turns rolling the dice by clicking the "Roll Dice" button.
The number rolled determines how many squares the player moves forward.
Landing on a ladder moves the player up to the square at the top of the ladder.
Landing on a snake moves the player down to the square at the tail of the snake.
The first player to reach square 100 wins.

Data Structures:
Graphs for the board layout.
Queues for player turns.
Random number generation for dice rolls.

Future Enhancements
Add a visual game board with player tokens.
Implement save/resume functionality.
Support for online multiplayer gameplay.
