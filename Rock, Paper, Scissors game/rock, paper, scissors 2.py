import tkinter as tk
import os
import random

def game(btn):
    global player_score, comp_score
    moves = ["Rock", "Paper", "Scissors"]
    player = btn.cget("text")
    computer = random.choice(moves)

    user_choice.config(text=player)
    comp_choice.config(text=computer)

    if (player == "Rock" and computer == "Paper") or (player == "Paper" and computer == "Scissors") or (player == "Scissors" and computer == "Rock"):
        winner_label.config(text="Computer wins!")
        comp_score += 1
    elif player == computer:
        winner_label.config(text="It's a draw!")
    else:
        winner_label.config(text="You win!")
        player_score += 1

    update_scores()

def update_scores():
    player_score_label.config(text=f"Your score: {player_score}")
    comp_score_label.config(text=f"Computer's score: {comp_score}")

def restart_game():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    update_scores()
    user_choice.config(text="(Select a move)")
    comp_choice.config(text="(Waiting)")
    winner_label.config(text="")

def on_hover(event):
    event.widget.config(bg="#9DAEB9")

def on_leave(event):
    event.widget.config(bg="#B4C5D1")

bg_color = "#232b31"
player_score = 0
comp_score = 0

root = tk.Tk()
root.geometry("760x640")
root.title("Rock, Paper, Scissors")
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(fill="both", expand=True)

label = tk.Label(main_frame, text="Rock, Paper and Scissors", font="Terminal 24 bold", padx=10, pady=10, bg="#B4C5D1")
label.pack(pady=(30, 20))

label2 = tk.Label(main_frame, text="Choose your move:", font="Courier 16", bg=bg_color, fg="white")
label2.pack(pady=20)

button_frame = tk.Frame(main_frame, bg=bg_color)
button_frame.pack(pady=10)


current_dir = os.path.dirname(__file__) # Getting the absolute path

rock_image = tk.PhotoImage(file=os.path.join(current_dir, "images", "rock.png"))

button1 = tk.Button(button_frame, text="Rock", image=rock_image, compound=tk.BOTTOM, font=("Courier 17 bold"), width=120, height=100, command=lambda: game(button1), cursor="hand2", border=6, activebackground="#B4C5D1", highlightcolor="#B4C5D1", bg="#B4C5D1")
button1.grid(row=0, column=0, padx=20)
button1.bind("<Enter>", on_hover)
button1.bind("<Leave>", on_leave)


paper_image = tk.PhotoImage(file=os.path.join(current_dir, "images", "paper.png"))

button2 = tk.Button(button_frame, text="Paper", image=paper_image, compound=tk.BOTTOM, font=("Courier 17 bold"), width=120, height=100, command=lambda: game(button2), cursor="hand2", border=6, activebackground="#B4C5D1", highlightcolor="#B4C5D1", bg="#B4C5D1")
button2.grid(row=0, column=1, padx=20)
button2.bind("<Enter>", on_hover)
button2.bind("<Leave>", on_leave)

scissors_image = tk.PhotoImage(file=os.path.join(current_dir, "images", "scissors.png"))

button3 = tk.Button(button_frame, text="Scissors", image=scissors_image, compound=tk.BOTTOM, font=("Courier 17 bold"), width=120, height=100, command=lambda: game(button3), cursor="hand2", border=6, activebackground="#B4C5D1", highlightcolor="#B4C5D1", bg="#B4C5D1")
button3.grid(row=0, column=2, padx=20)
button3.bind("<Enter>", on_hover)
button3.bind("<Leave>", on_leave)

restart_button = tk.Button(main_frame, text="Restart", font=("Courier 14"), width=10, height=1, command=restart_game, cursor="hand2", border=6, activebackground="#B4C5D1", highlightcolor="#B4C5D1", bg="#B4C5D1")
restart_button.pack(pady=10)

frame2 = tk.Frame(main_frame, bg=bg_color)
frame2.pack(pady=20)

user_label = tk.Label(frame2, text="Your move: ", font="Courier 16 bold", bg=bg_color, fg="white")
user_label.grid(row=0, column=0, padx=40, pady=10)

comp_label = tk.Label(frame2, text="Computer's move: ", font="Courier 16 bold", bg=bg_color, fg="white")
comp_label.grid(row=0, column=1, padx=40, pady=10)

user_choice = tk.Label(frame2, text="(Select a move)", font="Courier 16", bg=bg_color, fg="white")
user_choice.grid(row=1, column=0, padx=40, pady=(0, 10))

comp_choice = tk.Label(frame2, text="(Waiting)", font="Courier 16", bg=bg_color, fg="white")
comp_choice.grid(row=1, column=1, padx=40, pady=(0, 10))

score_frame = tk.Frame(main_frame, bg=bg_color)
score_frame.pack(pady=10)

player_score_label = tk.Label(score_frame, text=f"Your score: {player_score}", font="Courier 16", bg=bg_color, fg="white")
player_score_label.pack(side=tk.LEFT, padx=20)

comp_score_label = tk.Label(score_frame, text=f"Computer's score: {comp_score}", font="Courier 16", bg=bg_color, fg="white")
comp_score_label.pack(side=tk.RIGHT, padx=20)

result_frame = tk.Frame(main_frame, bg=bg_color)
result_frame.pack(pady=10)

winner_label = tk.Label(result_frame, text="", font="Courier 20 bold", bg=bg_color, fg="white")
winner_label.pack()

root.mainloop()
