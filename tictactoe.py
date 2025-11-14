import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("400x450")

        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Tic-Tac-Toe", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Current player display
        self.player_label = tk.Label(self.root, text=f"Current Player: {self.current_player}", font=("Arial", 12), fg="blue")
        self.player_label.pack(pady=5)

        # Game board frame
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=20)

        # Create 3x3 grid of buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(board_frame, text="", font=("Arial", 20), width=4, height=2,
                                   command=lambda idx=i*3+j: self.make_move(idx))
                button.grid(row=i, column=j, padx=2, pady=2)

                # Hover effect
                button.bind("<Enter>", lambda e, b=button: b.config(bg="lightgray"))
                button.bind("<Leave>", lambda e, b=button: b.config(bg="SystemButtonFace"))

                row.append(button)
            self.buttons.append(row)

        # Control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)

        reset_btn = tk.Button(control_frame, text="New Game", command=self.reset_game, bg="lightgreen")
        reset_btn.pack(side=tk.LEFT, padx=10)

        quit_btn = tk.Button(control_frame, text="Quit", command=self.root.quit, bg="lightcoral")
        quit_btn.pack(side=tk.LEFT, padx=10)

    def make_move(self, index):
        if not self.game_active or self.board[index] != "":
            return

        self.board[index] = self.current_player
        row, col = index // 3, index % 3
        self.buttons[row][col].config(
            text=self.current_player,
            state=tk.DISABLED,
            bg="lightyellow" if self.current_player == "X" else "lightblue"
        )

        if self.check_winner():
            self.game_active = False
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.disable_all_buttons()   # 🔥 Disable buttons when game ends
        elif self.check_tie():
            self.game_active = False
            messagebox.showinfo("Game Over", "It's a tie!")
            self.disable_all_buttons()   # 🔥 Disable buttons when game ends
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.player_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for combo in wins:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.current_player:
                for idx in combo:
                    row, col = idx // 3, idx % 3
                    self.buttons[row][col].config(bg="lightgreen")
                return True
        return False

    def check_tie(self):
        return "" not in self.board

    # ✅ Commit: Disable all buttons after win/tie
    def disable_all_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        self.player_label.config(text=f"Current Player: {self.current_player}")

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=tk.NORMAL, bg="SystemButtonFace")

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
