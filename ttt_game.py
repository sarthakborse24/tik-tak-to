import tkinter as tk

window = tk.Tk()
turn = "X"
def click(button):
    global turn
    button.config(text=turn,state="disabled")
    if turn=="X":
        turn = "O"
    else:
        turn = "X"
    label.config(text=f"{turn}'s Turn")     

window.title("tic tak toe game")
label = tk.Label(window,text="tic tak toe game",font=("arial bold",16))
label.pack()
frame = tk.Frame(window)
frame.pack()

for r in range(3):
    for c in range(3):
        btn = tk.Button(frame,text="",font=("Arial Bold",15),command=click,height=4,width=8)
        btn.grid(row=r,column=c)
        btn.config(command=lambda b=btn: click(b))
        
window.mainloop()