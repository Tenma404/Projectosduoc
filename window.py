import tkinter as tk
ventana=tk.Tk()
ventana.title("Primer Intento de Ventana")
ventana.geometry("500x500")

texto=tk.Label (ventana,text="HOLAAA BIENVENIDO A MI PRIMER VENTANA")
texto.pack(pady=20)

boton=tk.Button (ventana,text="CLICKEA AQUIII")
boton.pack()

ventana.mainloop()