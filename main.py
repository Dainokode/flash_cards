from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# window setup
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(10, 0, image=card_front, anchor=NW)
canvas.grid(row=1, column=1, columnspan=2)

# text
canvas.create_text(400, 150, fill="black", font=("arial", 40, "italic"), text="french")
canvas.create_text(400, 250, fill="black", font=("arial", 60, "bold"), text="trouve")


# buttons
w_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=w_button, highlightthickness=0)
wrong_button.grid(row=2, column=1, pady=15)


r_button = PhotoImage(file="./images/right.png")
right_button = Button(image=r_button, highlightthickness=0)
right_button.grid(row=2, column=2, pady=15)


# run program
window.mainloop()