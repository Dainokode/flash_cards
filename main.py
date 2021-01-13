from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


# csv to dataframe
data = pd.read_csv("data/french_words.csv")
words_to_learn = data.to_dict(orient="records")
current_card = {}


def random_card(button_id):
    global current_card
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    if button_id == 2:
        words_to_learn.remove(current_card)
    window.after(3000, show_translation)
    print(words_to_learn)



def show_translation():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
   


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
wrong_button = Button(image=w_button, highlightthickness=0, command=lambda:random_card(1))
wrong_button.grid(row=2, column=1, pady=15)


r_button = PhotoImage(file="./images/right.png")
right_button = Button(image=r_button, highlightthickness=0, command=lambda:random_card(2))
right_button.grid(row=2, column=2, pady=15)


random_card(3)
window.after(3000, show_translation)

# run program
window.mainloop()


# seulement,only
# police,police
# pensais,thought
# aide,help
# demande,request
# genre,kind
# mois,month
# frère,brother
# laisser,let
# car,because
# mettre,to put
# aucun,no
# laisse,leash
# eux,them
# ville,city
# chaque,each
# parlé,speak
# arrivé,come
# devrait,should
# bébé,baby
# longtemps,long time
# heures,hours
# vont,will
# pendant,while
# revoir,meet again
# aucune,any
# place,square
# parle,speak
# compris,understood
# savais,knew
# étaient,were
# attention,Warning
# voici,here is
# pourrais,could
# affaire,case
# donner,give
# type,type
# leurs,their
# donné,given
# train,train
# corps,body
# endroit,place
# yeux,eyes
# façon,way
# écoute,listen
# dont,whose
# trouve,find
# premier,first
# perdu,lost
# main,hand
# première,first
# côté,side
# pouvoir,power
# vieux,old
# sois,be
# tiens,here
# matin,morning
# tellement,so much
# enfant,child
# point,point
# venu,came
# suite,after
# pardon,sorry
# venez,come
# devant,in front of
# vers,towards
# minutes,minutes
# demandé,request
# chambre,bedroom
# mis,placed
# belle,beautiful
# droit,law
# aimerais,would like to
# aujourd'hui,today
# mari,husband
# cause,cause
# enfin,finally
# espère,hope
# eau,water
# attendez,Wait
# parti,left
# nouvelle,new
# boulot,job
# arrêter,Stop
# dirait,would say
# terre,Earth
# compte,account
# donne,given
# loin,far
# fin,end
# croire,believe
# chérie,sweetheart
# gros,large
# plutôt,rather
# aura,will have
# filles,girls
# jouer,to play
# bureau,office