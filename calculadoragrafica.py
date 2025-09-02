from tkinter import *
import numpy as np

ventana = Tk()
ventana.title("calculadora")
ventana.geometry("500x200")
ventana.resizable(0,0)

TextoUno = Label(ventana, text="valor1")
TextoDos = Label(ventana, text="valor2")
TextoUno.grid(row=0, column=0,padx=5,pady=5)
TextoDos.grid(row=0, column=0,padx=5,pady=5)
#entradas
entradauno = Entry(ventana)
entradaDos = Entry(ventana)
entradasuma = Entry (ventana, state="readonly")
entradaresta = Entry(ventana, state=DISABLED)
entradamultiplicacion = Entry(ventana, state=DISABLED)
entradadivision = Entry (ventana, state=DISABLED)
entradauno.grid(row=0, column=1,padx=5,pady=5)
entradaDos.grid(row=0, column=4,padx=5,pady=5)
entradasuma.grid(row=1, column=1,padx=5,pady=5)
entradaresta.grid(row=2, column=1,padx=5,pady=5)
entradamultiplicacion.grid(row=3, column=1,padx=5,pady=5)
entradadivision.grid(row=4, column=1,padx=5,pady=5)
#botones 
botonsuma = Button(ventana, text="suma", width=8, height=1, command=lambda:clickBotonsuma(entradauno.get(), entradaDos.get()))
botonresta = Button(ventana, text="resta", width=8, height=1, command=lambda:clickBotonresta(entradauno.get(), entradaDos.get()))
botonmultiplicacion = Button(ventana, text="multiplicar", width=8, height=1, command=lambda:clickBotonmultiplicacion(entradauno.get(), entradaDos.get()))
botondivision = Button(ventana, text="divsion", width=8, height=1, command=lambda:clickBotondivision(entradauno.get(), entradaDos.get()))
botonsuma.grid(row=1, column=0,padx=5,pady=5)
botonresta.grid(row=2, column=0,padx=5,pady=5)
botonmultiplicacion.grid(row=3, column=0,padx=5,pady=5)
botondivision.grid(row=4, column=0,padx=5,pady=5)
#funciones calculadora
def clickBotonsuma(x,y):
    entradasuma.configure(state=NORMAL)
    entradasuma.delete(0,END)
    entradasuma.insert(0,f"{int(x)+int(y)}")
    entradasuma.configure(state=DISABLED)
    botonsuma.configure(background="DARKGRAY")
def clickBotonresta(x,y):
    entradaresta.configure(state=NORMAL)
    entradaresta.delete(9,END)
    entradaresta.insert(0,f"{int(x)-int(y)}")
    entradaresta.configure(state=DISABLED)
    botonresta.configure(background="DARKGRAY")
def clickBotonmultiplicacion(x,y):
    entradamultiplicacion.configure(state=NORMAL)
    entradamultiplicacion.delete(0,END)
    entradamultiplicacion.insert(0,f"{int(x)*int(y)}")
    entradamultiplicacion.configure(state=DISABLED)
    botonmultiplicacion.configure(background="DARKGRAY")
def clickBotondivision(x,y):
    entradadivision.configure(state=NORMAL)
    entradadivision.delete(0,END)
    entradadivision.insert(0,f"{np.double(x)/np.double(y)}")
    entradadivision.configure(state=DISABLED)
    botondivision.configure(background="DARKGRAY")
    
    
ventana.mainloop()