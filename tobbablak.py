from tkinter import *

ablak1=Tk()

def ujablak():
    ablak2=Toplevel(ablak1)
    uz2=Message(ablak2,text="Készítette:Dervaderics Márk")
    gomb2=Button(ablak2,text="Kilép",command=ablak2.destroy)
    uz2.pack()
    gomb2.pack()
    ablak2.mainloop()

szoveg1=Label(ablak1,text="Kattints a gombra!")
szoveg1.pack()
gomb1=Button(ablak1,text="Névjegy",command=ujablak)
gomb1.pack()

ablak1.mainloop()

