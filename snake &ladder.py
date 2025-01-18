import tkinter as tk
import random

class SnakeAndLadderGame:
    def __init__(self):
        # Define snakes and ladders
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

        self.players = []
        self.positions = {}
        self.current_player_index = 0
        self.winner = None

    def add_player(self, player_name):
        """Add a new player to the game."""
        if player_name not in self.players:
            self.players.append(player_name)
            self.positions[player_name] = 0
            return True
        return False

    def roll_dice(self):
        """Roll the dice and return a random number between 1 and 6."""
        return random.randint(1, 6)

    def move_player(self, player_name, dice_value):
        """Move a player based on the dice roll."""
        current_position = self.positions[player_name]
        new_position = current_position + dice_value

        if new_position > 100:
            return current_position  # Can't move past 100

        # Check for snakes or ladders
        new_position = self.snakes.get(new_position, new_position)
        new_position = self.ladders.get(new_position, new_position)

        self.positions[player_name] = new_position
        return new_position

    def get_current_player(self):
        """Return the name of the current player."""
        return self.players[self.current_player_index]

    def next_turn(self):
        """Move to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def check_winner(self):
        """Check if there's a winner."""
        for player, position in self.positions.items():
            if position == 100:
                self.winner = player
                return player
        return None


class SnakeAndLadderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")

        # Initialize the game logic
        self.game = SnakeAndLadderGame()

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        """Create the GUI layout."""
        # Add player section
        player_frame = tk.Frame(self.root, padx=10, pady=10)
        player_frame.pack()

        tk.Label(player_frame, text="Player Name:").grid(row=0, column=0, padx=5, pady=5)
        self.player_entry = tk.Entry(player_frame)
        self.player_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(player_frame, text="Add Player", command=self.add_player).grid(row=0, column=2, padx=5, pady=5)

        # Dice roll and turn section
        turn_frame = tk.Frame(self.root, padx=10, pady=10)
        turn_frame.pack()

        self.turn_label = tk.Label(turn_frame, text="Turn: None", font=("Arial", 14))
        self.turn_label.pack(pady=5)

        self.dice_label = tk.Label(turn_frame, text="Dice: 0", font=("Arial", 14))
        self.dice_label.pack(pady=5)

        tk.Button(turn_frame, text="Roll Dice", command=self.roll_dice).pack(pady=5)

        # Game board and positions
        self.board_frame = tk.Frame(self.root, padx=10, pady=10)
        self.board_frame.pack()

        self.position_label = tk.Label(self.board_frame, text="Positions: None", font=("Arial", 12))
        self.position_label.pack()

    def add_player(self):
        """Add a player to the game."""
        player_name = self.player_entry.get().strip()
        if not player_name:
            tk.messagebox.showwarning("Input Error", "Player name cannot be empty.")
            return

        if self.game.add_player(player_name):
            tk.messagebox.showinfo("Success", f"Player '{player_name}' added successfully.")
            self.update_positions()
            if len(self.game.players) == 1:
                self.turn_label.config(text=f"Turn: {player_name}")
        else:
            tk.messagebox.showerror("Error", f"Player '{player_name}' already exists.")

    def roll_dice(self):
        """Roll the dice and move the current player."""
        if not self.game.players:
            tk.messagebox.showerror("Error", "No players added to the game.")
            return

        if self.game.winner:
            tk.messagebox.showinfo("Game Over", f"The game is over. '{self.game.winner}' won!")
            return

        current_player = self.game.get_current_player()
        dice_value = self.game.roll_dice()
        self.dice_label.config(text=f"Dice: {dice_value}")

        new_position = self.game.move_player(current_player, dice_value)
        self.update_positions()

        # Check if the current player has won
        winner = self.game.check_winner()
        if winner:
            tk.messagebox.showinfo("Winner", f"'{winner}' wins the game!")
            self.turn_label.config(text=f"Winner: {winner}")
        else:
            # Move to the next player's turn
            self.game.next_turn()
            next_player = self.game.get_current_player()
            self.turn_label.config(text=f"Turn: {next_player}")

    def update_positions(self):
        """Update the position display."""
        positions = ", ".join(f"{player}: {pos}" for player, pos in self.game.positions.items())
        self.position_label.config(text=f"Positions: {positions}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeAndLadderGUI(root)
    root.mainloop()
