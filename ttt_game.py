import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe Game")

turn = "X"
buttons = []

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


def click(button):
    global turn

    button.config(text=turn, state="disabled")

    if check_winner():
        label.config(text=f"{turn} Wins!")
        disable_all()
        return

    if check_draw():
        label.config(text="It's a Draw!")
        return

    turn = "O" if turn == "X" else "X"
    label.config(text=f"{turn}'s Turn")


def disable_all():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")


label = tk.Label(window, text="X's Turn", font=("Arial Bold", 16))
label.pack()

frame = tk.Frame(window)
frame.pack()

for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(frame, text="", font=("Arial Bold", 15),
                        height=4, width=8)
        btn.grid(row=r, column=c)
        btn.config(command=lambda b=btn: click(b))
        row.append(btn)
    buttons.append(row)

window.mainloop()