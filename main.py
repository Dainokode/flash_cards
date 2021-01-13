from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


current_cards = {}
french_words = {}


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_words = original_data.to_dict(orient="records")
else:
    french_words = data.to_dict(orient="records")



def random_card():
    global current_cards
    current_cards = random.choice(french_words)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_cards["French"], fill="black") 
    window.after(3000, show_translation)
    print(current_cards)



def is_known():
    french_words.remove(current_cards)
    df = pd.DataFrame(french_words)
    df.to_csv("data/words_to_learn.csv", index=False)
    random_card()



def show_translation():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_cards["English"], fill="white")
   


# window setup
window = Tk()
window.title("Flash French")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(10, 0, image=card_front, anchor=NW)
canvas.grid(row=1, column=1, columnspan=2)


# canvas text
card_title = canvas.create_text(400, 150, fill="black", font=("arial", 40, "italic"), text="")
card_text = canvas.create_text(400, 250, fill="black", font=("arial", 60, "bold"), text="")


# buttons
w_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=w_button, highlightthickness=0, command=random_card)
wrong_button.grid(row=2, column=1, pady=15)


r_button = PhotoImage(file="./images/right.png")
right_button = Button(image=r_button, highlightthickness=0, command=is_known)
right_button.grid(row=2, column=2, pady=15)


random_card()
window.after(3000, show_translation)

# run program
window.mainloop()
