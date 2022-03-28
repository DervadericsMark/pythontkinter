'''
Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre
álló bor. Kérd be a bor mennyiségét literben, majd a hordó összes szükséges adatát cmben.
Adj tájékoztatást, hogy hány literes a hordó, és hogy belefér-e a hordóba a bor! Ha
belefér, akkor add meg, hogy mennyi férne még bele! Írd ki százalékosan is a
telítettséget! Az adatokat egészre kerekítve írd ki!
'''
from tkinter import *
foablak=Tk()

hordosugara=Label(foablak,text="A hordó sugara (dm-ben):")
hordosugara.grid(row=0,column=0)

sugarmezo=Entry(foablak)
sugarmezo.grid(row=0,column=1)

hordomagassaga=Label(foablak,text="A hordó magassága (dm-ben):")
hordomagassaga.grid(row=1,column=0)

magassagmezo=Entry(foablak)
magassagmezo.grid(row=1,column=1)

foablak.mainloop()