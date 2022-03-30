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
    sugar=int(sugarmezo.get())
    magassag=int(magassagmezo.get())
    terfogat=math.pi*sugar**2*magassag
    


foablak=Tk()

hordosugara=Label(foablak,text="A hordó sugara (dm-ben):")
hordosugara.grid(row=0,column=0)

sugarmezo=Entry(foablak)
sugarmezo.grid(row=0,column=1)

hordomagassaga=Label(foablak,text="A hordó magassága (dm-ben):")
hordomagassaga.grid(row=1,column=0)

magassagmezo=Entry(foablak)
magassagmezo.grid(row=1,column=1)

hordoliter=Label(foablak,text="A hordó térfogata literben:")
hordoliter.grid(row=2,column=0)

hordolitermezo=Entry(foablak)
hordolitermezo.grid(row=2,column=1)

bormennyiseg=Label(foablak,text="A bor mennyisége:")
bormennyiseg.grid(row=4,column=0)

bormennyiseg_mezo=Entry(foablak)
bormennyiseg_mezo.grid(row=4,column=1)

gomb1=Button(foablak,text="Kiszámol")
gomb1.grid(row=5,column=1)

foablak.mainloop()