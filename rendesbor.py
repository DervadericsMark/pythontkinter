'''
Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre
álló bor. Kérd be a bor mennyiségét literben, majd a hordó összes szükséges adatát cmben.
Adj tájékoztatást, hogy hány literes a hordó, és hogy belefér-e a hordóba a bor! Ha
belefér, akkor add meg, hogy mennyi férne még bele! Írd ki százalékosan is a
telítettséget! Az adatokat egészre kerekítve írd ki!
'''

from tkinter import *
import math

def szamolas():
    hordoba_fer.delete(0, END)
    beleferemezo.delete(0, END)
    megbelefernemezo.delete(0, END)
    sugar=int(sugarmezo.get())
    magassag=int(hordomagassaga_mezo.get())
    bekert_bor = int(bormennyiseg_mezo.get())
    korterulet=sugar*sugar*math.pi
    cm3=korterulet*magassag
    dm3=cm3/1000
    hordolitermennyisege=dm3
    hordolitermennyisege = round(hordolitermennyisege, 0)
    hordolitermennyisege=int(hordolitermennyisege)
    hordoba_fer.insert(0, "{:.0f}".format(hordolitermennyisege) + " liter!")
    if bekert_bor > hordolitermennyisege:
        beleferemezo.insert(0, "Nem fér bele :(")
    else:
        meg_belefer = hordolitermennyisege - bekert_bor
        beleferemezo.insert(0, "Belefér! :)")
        megbelefernemezo.insert(0, f"{meg_belefer} liter")

foablak=Tk()
foablak.title("Hordó")

hordosugara=Label(foablak,text="A hordó sugara (cm-ben):")
hordosugara.grid(row=0,column=0)

sugarmezo=Entry(foablak)
sugarmezo.grid(row=0,column=1)

hordomagassaga=Label(foablak,text="A hordó magassága (cm-ben):")
hordomagassaga.grid(row=1,column=0)

hordomagassaga_mezo=Entry(foablak)
hordomagassaga_mezo.grid(row=1,column=1)

bormennyiseg=Label(foablak,text="A bor mennyisége:")
bormennyiseg.grid(row=2,column=0)

bormennyiseg_mezo=Entry(foablak)
bormennyiseg_mezo.grid(row=2,column=1)

gomb1=Button(foablak,text="Kiszámol", command=szamolas)
gomb1.grid(row=3,column=1)

hordobafer=Label(foablak,text="A hordóba még fér:")
hordobafer.grid(row=4,column=0)

hordoba_fer = Entry(foablak)
hordoba_fer.grid(row=4, column=1)

belefere=Label(foablak,text="Bele fér-e a bor:")
belefere.grid(row=5,column=0)

beleferemezo=Entry(foablak)
beleferemezo.grid(row=5,column=1)

megbeleferne=Label(foablak,text="Még beleférne:")
megbeleferne.grid(row=6,column=0)

megbelefernemezo=Entry(foablak)
megbelefernemezo.grid(row=6,column=1)
foablak.mainloop()