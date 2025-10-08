import tkinter as tk
import math


root = tk.Tk()
root.title("Tic-Tac-Toe AI")

board = [" " for _ in range(9)]
buttons = []

def check_winner(board, player):
    
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_full(board):
    return " " not in board

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = None
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        if check_winner(board, "X"):
            tk.messagebox.showinfo("Game Over", "You Win!")
            reset_board()
            return
        elif is_full(board):
            tk.messagebox.showinfo("Game Over", "Draw!")
            reset_board()
            return
        ai = best_move(board)
        board[ai] = "O"
        buttons[ai].config(text="O", state="disabled")
        if check_winner(board, "O"):
            tk.messagebox.showinfo("Game Over", "AI Wins!")
            reset_board()
        elif is_full(board):
            tk.messagebox.showinfo("Game Over", "Draw!")
            reset_board()

def reset_board():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
