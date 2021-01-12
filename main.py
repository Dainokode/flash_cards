from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# window setup
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(10, 0, image=card_front, anchor=NW)
canvas.grid(row=1, column=1, columnspan=1)


# run program
window.mainloop()