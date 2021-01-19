from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


# -------------------- PROGRAM LOGIC -------------------- #
data = pd.read_csv("data/french_words.csv")
words_list = pd.DataFrame.to_dict(data, orient="records")
random_word = random.choice(words_list)


def next_card():
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_word["French"])
    window.after(3000, show_translation)


def show_translation():
    canvas.itemconfig(canvas_image, image=bg_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")

# -------------------- UI SETUP -------------------- #
# Window setup
window = Tk()
window.title("French Flash Cards")
window.config(bg=BACKGROUND_COLOR)


# Canvas setup
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas images
bg_front = PhotoImage(file="images/card_front.png")
bg_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(405, 263, image=bg_front)
# place canvas
canvas.grid(row=0, column=0, columnspan=2, pady=30, padx=50)
# insert text
title = canvas.create_text(400, 150, font=("arial", 40, "italic"), text="French")
word = canvas.create_text(400, 253, font=("arial", 60, "bold"), text="Trouve")


# Buttons
r_button_image = PhotoImage(file="images/right.png")
r_button = Button(image=r_button_image, highlightthickness=0, command=next_card)
r_button.grid(row=1, column=1, pady=30)


w_button_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=w_button_image, highlightthickness=0, command=next_card)
w_button.grid(row=1, column=0)


next_card()

# Run program
window.mainloop()