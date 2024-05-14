from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        else:
            if check_winner() == "Tie":
                label.config(text="Tie!")
            else:
                label.config(text=(player + " wins"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner([buttons[row][0], buttons[row][1], buttons[row][2]])
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            highlight_winner([buttons[0][column], buttons[1][column], buttons[2][column]])
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True

    elif not empty_spaces():
        return "Tie"

    return False

def highlight_winner(cells):
    for cell in cells:
        cell.config(bg="green")

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('Comic Sans MS', 20))
label.pack(side="top")

reset_button = Button(text="Restart", font=('Comic Sans MS', 14), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Consolas', 20), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
        buttons[row][column].config(bg="#D3D3D3")

window.mainloop()