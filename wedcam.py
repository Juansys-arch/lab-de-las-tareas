import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import imutils
import cv2

ventana = tk.Tk()
ventana.geometry("400x370")
ventana.resizable(0,0)
ventana.title("Iniciar webcam")

def camara():
    global capture
    capture = cv2.VideoCapture(0)
    iniciar()
    
def iniciar():
    global capture
    if capture is not None:
        ret, frame = capture.read()
        if ret == True:
            frame = imutils.resize(frame, width=311)
            frame = imutils.resize(frame, height=241)
            ImageCamara = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im= Image.fromarray(ImageCamara)
            img = ImageTk.PhotoImage(image= im)
            LImagen.configure(image=img)
            LImagen.image = img 
            LImagen.after(1,iniciar)
        else:
            LImagen.image =""
            capture.release()
            
Bcamara = tk.Button(ventana, text="iniciar camara", command=camara)
Bcamara.place(x=150,y=330,width=90,height=23)

LImagen = tk.Label(ventana, background="gray")
LImagen.place(x=50,y=50,width=300,height=240)

ventana.mainloop()

