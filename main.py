from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# Window setup
window = Tk()
window.title("French Flash Cards")
window.config(bg=BACKGROUND_COLOR)


# Canvas setup
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas image
bg_white = PhotoImage(file="images/card_front.png")
canvas.create_image(405, 280, image=bg_white)
# place canvas
canvas.grid(row=0, column=0, columnspan=2, pady=30, padx=50)
# insert text
canvas.create_text(400, 150, font=("arial", 40, "italic"), text="French")
canvas.create_text(400, 253, font=("arial", 60, "bold"), text="Trouve")


# Buttons
r_button_image = PhotoImage(file="images/right.png")
r_button = Button(image=r_button_image, highlightthickness=0)
r_button.grid(row=1, column=1, pady=30)


w_button_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=w_button_image, highlightthickness=0)
w_button.grid(row=1, column=0)

# Run program
window.mainloop()