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
#ventana principalf
#----------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-----------------------
#frame de graficacion
#-----------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=480)
frame_graficacion.place(x=10,y=10)

#creacion canvas

c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)


#lineas de guia
#lineas
linea_central_horizontal= c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="green")
linea_vertical= c.create_line(BASE/2,0,BASE/2,ALTURA, fill="green")

"""#triangulo base
polig_1= c.create_polygon(BASE/2,ALTURA/2,BASE-120,ALTURA,BASE/2-90,ALTURA,fill="thistle")

#arcos

arco_1 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=90, extent=45, fill="red")
arco_2 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=270, extent=45, fill="red")
arco_3 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=180, extent=45, fill="red")
arco_4 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=360, extent=45, fill="red")


#rectangulo
rec_1 = c.create_rectangle(BASE/2-100,BASE/2+200,360,ALTURA-20, fill="cyan")"""


#generar 100 circulos de radio = 10
for i in range(100):
    #generar color aleatorio
    color = "#"
    for i in range(6):
        color = color + random.choice("0123456789ABCDEF")
    #generar valor de x e y aleatorio
    radio = random.randint(5,25)
    x = random.randint(0, BASE-2*radio)
    y = random.randint(0, ALTURA-2*radio)
    

    #dibujamos el circulo
    circulo = c.create_arc(x,y,x+2*radio,y+2*radio, start=40, extent=270, fill=color)
    ojo = c.create_oval(x,y,x+3, y+3, fill=color)
# agregar nave
img_nave = PhotoImage(file="img/nave2.png")

#arco
radio = random.randint(5,25)
arco = c.create_arc(BASE/2-radio,ALTURA/2-radio, BASE/2+radio, ALTURA/2+radio, start=0,extent=0, fill="blue")

#----------------------
# FRAME DE CONTROLES ,
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=480)
frame_controles.place(x=10, y=260)


#barra de deslizamientos
barra_deslizamiento = Scale(frame_controles, label="angulo", from_=0, to=360, orient="horizontal", length=460, tickinterval=45,
command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)



# DESPLEGAR VENTANA 
ventana_principal.mainloop()




