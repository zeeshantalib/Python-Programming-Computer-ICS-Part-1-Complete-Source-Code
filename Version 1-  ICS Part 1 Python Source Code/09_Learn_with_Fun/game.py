import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#2C3E50")
        self.current_player = "X"
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", 
                              font=("Segoe UI", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
        self.label.grid(row=0, column=0, columnspan=3, pady=15)

        button_style = {
            "font": ("Segoe UI", 24, "bold"),
            "width": 5,
            "height": 2,
            "bd": 0,
            "relief": "ridge",
            "bg": "#34495E",
            "fg": "#ECF0F1",
            "activebackground": "#1ABC9C",
            "activeforeground": "#2C3E50",
            "cursor": "hand2",
        }
        
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, **button_style,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i+1, column=j, padx=8, pady=8)
                self.buttons[i][j] = btn
                
        self.reset_button = tk.Button(self.root, text="Reset", font=("Segoe UI", 14, "bold"),
                                      bg="#E74C3C", fg="white", activebackground="#C0392B",
                                      activeforeground="white", cursor="hand2",
                                      command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=20, ipadx=30, ipady=8)
    
    def on_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.current_player
            if self.current_player == "X":
                btn.config(fg="#1ABC9C")  # Teal for X
            else:
                btn.config(fg="#E67E22")  # Orange for O
                
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins! 🎉")
                self.highlight_winner()
                self.disable_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw! 🤝")
                self.disable_buttons()
            else:
                self.switch_player()
                self.label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        b = self.buttons
        lines = [
            # rows
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            # cols
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            # diagonals
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]
        ]
        for line in lines:
            if b[line[0][0]][line[0][1]]["text"] == b[line[1][0]][line[1][1]]["text"] == b[line[2][0]][line[2][1]]["text"] != "":
                self.winning_line = line
                return True
        return False
    
    def highlight_winner(self):
        for r,c in self.winning_line:
            self.buttons[r][c].config(bg="#F1C40F", fg="#2C3E50", font=("Segoe UI", 26, "bold"))
    
    def is_draw(self):
        return all(btn["text"] != "" for row in self.buttons for btn in row)
    
    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def reset_game(self):
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s turn")
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal", bg="#34495E", fg="#ECF0F1", font=("Segoe UI", 24, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
