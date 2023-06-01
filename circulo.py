from tkinter import*
import random

#-----------------
#variables globales
#------------------

BASE=480
ALTURA=260
RADIO= 50

#funcio para modificar
def modificar_arco(angulo):
    c.itemconfig(arco, extent= angulo)
#----------------------
#ventana principal
#----------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D-  lineas rectas")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-----------------------
#frame de graficacion
#-----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=260)
frame_graficacion.place(x=10,y=10)

#creacion canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)


#arco
radio = random.randint(5,25)
arco = c.create_arc(BASE/2-radio,ALTURA/2-radio, BASE/2+radio, ALTURA/2+radio, start=0,extent=0, fill="blue")

#----------------------
# FRAME DE CONTROLES ,
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=230)
frame_controles.place(x=10, y=260)


#barra de deslizamientos
barra_deslizamiento = Scale(frame_controles, label="angulo", from_=0, to=360, orient="horizontal", length=460, tickinterval=45,
command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)



# DESPLEGAR VENTANA 
ventana_principal.mainloop()




