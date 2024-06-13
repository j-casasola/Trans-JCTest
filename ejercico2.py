from tkinter import *
#Pantalla
interface = Tk()
interface.config(width=500, height=500)
interface.title("Pantalla Nueva")
interface.configure(bg="green")
#Función
def copiar():
    global saldo
    valor=float(form_Ingreso.get()) #obtenemos el valor del form
    #saldo=valor #decimos que copie el valor (se podría sumar algo por ejemplo)
    saldo=valor+10
    resultado_saldo = Label(text=f"{saldo}") #mostramos el resultado
    resultado_saldo.place(x=200, y=200)
#Form
form_Ingreso = Entry()
form_Ingreso.place(x=50, y=60, width=100)
#Label
nombre_valor = Label(text="Ingrese valor")
nombre_valor.place(x=50, y=20)
#Botón
boton_copiar = Button(text="Copiar", command=copiar)
boton_copiar.place(x=60, y=200)
interface.mainloop()
