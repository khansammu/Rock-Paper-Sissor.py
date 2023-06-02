import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

def create_gui():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors")

    rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
    rock_button.pack()

    paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
    paper_button.pack()

    scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))
    scissors_button.pack()

    window.mainloop()

create_gui()
