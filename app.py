import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random

# Game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [""] * 9
        self.current_player = "X"  # Player starts as 'X'
        self.buttons = []
        self.create_loading_page()

    # Loading page with "Start Game" button and an image
    def create_loading_page(self):
        self.loading_frame = tk.Frame(self.root)
        self.loading_frame.pack()

        # Add an image (Assume the image is named 'tic_tac_toe.png')
        try:
            self.image = PhotoImage(file="tic_tac_toe.png")
            image_label = tk.Label(self.loading_frame, image=self.image)
            image_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading image: {e}")
            image_label = tk.Label(self.loading_frame, text="Tic-Tac-Toe")
            image_label.pack(pady=20)

        welcome_label = tk.Label(self.loading_frame, text="Welcome to Tic-Tac-Toe", font=("Arial", 16))
        welcome_label.pack(pady=10)

        start_button = tk.Button(self.loading_frame, text="Start Game", command=self.start_game, width=20, height=2)
        start_button.pack(pady=10)

    # Start game, remove loading page and show game board
    def start_game(self):
        self.loading_frame.pack_forget()  # Remove loading page
        self.create_board()

    # Create the Tic-Tac-Toe board
    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        for i in range(9):
            button = tk.Button(self.board_frame, text="", width=10, height=3,
                               font=("Arial", 20), command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    # Handle button clicks for moves
    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,
                                       fg="blue" if self.current_player == "X" else "red")
            if self.check_winner():
                self.highlight_winner(self.winning_combination)
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    # Check for a winner
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                self.winning_combination = condition
                return True
        return False

    # AI makes a move
    def ai_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.on_click(move)

    # Reset the game board
    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", fg="black", bg="SystemButtonFace")
        self.current_player = "X"

    # Highlight the winning combination
    def highlight_winner(self, combination):
        for index in combination:
            self.buttons[index].config(bg="yellow")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
