from tkinter import*
from tkinter import font

root=Tk()
MFrame=Frame()
root.title ("Ventana de prueba")
root.resizable(1,1)
root.iconbitmap("Ico.ico")
root.config(bg="white")


MFrame.pack(fill="both", expand="True")
MFrame.config(width="650", height="400")



Label(MFrame, text="hola world", fg="blue", font=("comic sans", 14)).place(x=1,y=1)
Nlabel=Label(MFrame, text="Nombre: ").place(x=10, y=10)
root.mainloop()

