from tkinter import *
import tkinter as tk
from tkinter import messagebox
from marvel import *
import json

naam = rasuper()
print(naam)
x=0
z=0
punten=25
uitslag = 0
scores=[]


def reset():
    """Functie voor het opnieuw ophalen en uitvoeren van andere functionaliteiten"""
    global x, z, punten, naam, uitslag
    x=0
    z=0
    punten=25
    L['text'] = 'Aantal Hints:0'
    hoeveelPunten['text'] = 'Aantal punten: 25'
    R['text'] = 'Aantal fout geraden:0'
    hint1['text'] = ''
    hint2['text'] = ''
    hint3['text'] = ''
    hint4['text'] = ''
    hint.counter=0
    raden.counter=0
    newHero()
    rasuper()
    naam=rasuper()
    antwoord.delete(0, END)
    Naam.delete(0,END)
    uitslag=0

def hint():
    """Returned aantal berekende punten en aantal gebruikte hints"""
    global x
    hint.counter+=1
    L['text'] = 'Aantal Hints:' + str(hint.counter)
    x=hint.counter
    x=x*-3
    aantalPunten = punten+x-z
    hoeveelPunten['text'] = 'Aantal punten: ' + str(aantalPunten)
    if aantalPunten <= 0:
        minimaalAantalPunten()
    return x

def minimaalAantalPunten():
    """Na 0 punten word er een pop-up laten zien, met de vraagstelling doorgaan of niet"""
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Je hebt het antwoord niet geraden, Wilt u opnieuw spelen?', icon='warning')
    if MsgBox == 'no':
        window.destroy()
    else:
        tk.messagebox.showinfo('Return', 'Het nieuwe spel word gestart.')
        reset()

def raden():
    """Kijkt of antwoord goed of fout is,op basiss daarvan gaan er ounten van af of komt er een pop up met een vraagstelling"""
    global z,uitslag
    if naam == antwoord.get():
        h= int(punten+x-z)
        uitslag+=h
        aantalPunten = punten+x-z
        hoeveelPunten['text'] = 'Aantal punten: ' + str(aantalPunten)
        puntenBijElkaar['text'] = 'Totaal aantal punten vorige ronden: ' + str(uitslag)
        scoreboard()
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Goed geraden! Wilt u opnieuw spelen?', icon='warning')
        if MsgBox == 'no':
            window.destroy()
        else:
            tk.messagebox.showinfo('Return', 'Het nieuwe spel word gestart.')
            reset()
    else:
        raden.counter +=1
        R['text'] = 'Aantal fout geraden: ' + str(raden.counter)
        z=raden.counter
        aantalPunten = punten+x-z
        hoeveelPunten['text'] = 'Aantal punten: ' + str(aantalPunten)
        if aantalPunten==0:
            puntenBijElkaar['text'] = 'Totaal aantal punten vorige ronden: ' + str(uitslag)
            minimaalAantalPunten()
        return z
def bhint():
    """laat een beschrijvings hint zien"""
    beschrijvingshints = rasdes()
    if beschrijvingshints == ['']:
        hint1['text'] = 'sorry geen beschrijving bij deze held!'
    else:
        for herodes in beschrijvingshints:
            hint1['text'] = herodes

def chint():
    """Laat een comic hint zien"""
    comicsHints = racomic()
    if not comicsHints:
        hint2['text'] = 'sorry geen beschrijving bij deze held!'
    else:
        hint2['text'] = comicsHints

def ehint():
    """laat een event hint zien"""
    eventHints = raevent()
    if not eventHints:
        hint3['text'] = 'sorry geen beschrijving bij deze held!'
    else:
        hint3['text'] = eventHints

def shint():
    """Laat een serie hint zien"""
    serieHints = raserie()
    if not serieHints:
        hint4['text'] = 'sorry geen beschrijving bij deze held!'
    else:
        hint4['text'] = serieHints

def gemengdb():
    """Roept 2 functionaliteiten aan door op de knop te drukken"""
    # hint()
    bhint()

def gemengdc():
    """Roept 2 functionaliteiten aan door op de knop te drukken"""
    hint()
    chint()

def gemengde():
    """Roept 2 functionaliteiten aan door op de knop te drukken"""
    hint()
    ehint()

def gemengds():
    """Roept 2 functionaliteiten aan door op de knop te drukken"""
    hint()
    shint()

def scoreboard():
    """Laat de hoogste score met naam er bij zien(word gereset naa het opnieuw opstaren van de programma)"""
    global scores
    read()
    write()
    scores.clear()

def write():
    datascores={'naam': Naam.get(),
                'score': uitslag}
    scores.append(datascores)
    with open('highscore.json', 'w', encoding='utf-8') as json_write:
        json.dump(scores, json_write, indent=4)

def read():
    with open('highscore.json', 'r', encoding='utf-8') as JSON_file:
        data = json.load(JSON_file)
        hoogste = 0
        lst=[]
        while True:
            for x in data:
                scores.append(x)
            break
        for getal in scores:
            getallen =lst.append(getal['score'])
            positie=lst.index(max(lst))
            hoogste=max(lst)
            naampos = data[positie]['naam']
            score['text'] = 'naam:', naampos[0:10], 'score:', hoogste



window = Tk()
hint.counter = 0
raden.counter=0


filename = PhotoImage(file = "monkimage.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.geometry('770x425')
window.resizable(False,False)

labelNaam = Label(window, text="Wat is uw naam?")
labelNaam.grid(row=1, column=1,  pady=4)

Naam = Entry(window)
Naam.grid(row=1, column=2, pady=4)

LabelAntwoord = Label(window, text="Vul uw antwoord in:")
LabelAntwoord.grid(row=3, column=1, pady=4)

antwoord = Entry(window, text='Vul het antwoord hier in')
antwoord.grid(row=3, column=2, pady=4)

gok = Button (window, text = "Raden", command = raden)
gok.grid(row=3, column=3, pady=4)

HintBeschrijving= Button(window, text="Hint Beschrijving", command = gemengdb)
HintBeschrijving.grid(row=5, column=0, pady=4)

HintComic= Button(window, text="Hint uit de Comics", command = gemengdc)
HintComic.grid(row=6, column=0, pady=4)

HintEvent= Button(window, text="Hint van een Event", command = gemengde)
HintEvent.grid(row=7, column=0, pady=4)

HintSerie= Button(window, text="Hint Uit de serie?", command = gemengds)
HintSerie.grid(row=8, column=0, pady=4)

hint1 = Label(window, text="")
hint1.grid(row=5, column=1, columnspan=10, pady=4)
hint2 = Label(window, text="")
hint2.grid(row=6, column=1, columnspan=10, pady=4)
hint3 = Label(window, text="")
hint3.grid(row=7, column=1, columnspan=10, pady=4)
hint4= Label(window, text="")
hint4.grid(row=8, column=1, columnspan=10, pady=4)


L = Label(window, text="Aantal hints: 0")
L.grid(row=12, column=0, pady=4)

R = Label(window, text="Aantal keer fout geraden: 0")
R.grid(row=12, column=1, pady=4)

hoeveelPunten = Label(window, text="Aantal punten: 25")
hoeveelPunten.grid(row=12, column=3, columnspan= 2, pady=4)

puntenBijElkaar = Label(window, text="Totaal aantal punten: 0")
puntenBijElkaar.grid(row=14, column=3, pady=4)

score = Label(window, height=2, width=25, text="")
score.grid(row=1, column=9, columnspan=3, pady=4)

read()
scores.clear()
window.mainloop()