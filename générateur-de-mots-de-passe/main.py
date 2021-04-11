import string
from random import randint, choice
from tkinter import *

color="#ABD9F9"
colortext ="#4A07FB"

def generateur():
    min = 20
    max = 20
    caracter = string.ascii_letters + string.punctuation + string.digits

    mdp = "".join(choice(caracter) for x in range(randint(min, max)))
    password.delete(0,END)
    password.insert(0,mdp)

root=Tk()
root.title("Générateur mdp")
root.minsize(480,360)
root.config(background=color)

frame =Frame(bg = color,)

title=Label(frame, text="MOT DE PASSE", font=("helvetica", 25), bg=color, fg=colortext)
title.pack()

password = Entry(frame, font=("arial", 15), bg="white", fg=colortext,width= 30, exportselection=0)
password.pack(fill=X)

sub_title=Label(frame, text=" ", font=("helvetica", 25), bg=color, fg=colortext)
sub_title.pack()

butom=Button(frame, text="Générer", font=("helvetica", 20), bg="grey",
             fg=colortext, command= generateur)
butom.pack(fill=X)

frame.pack(expand=YES)


root.mainloop()
