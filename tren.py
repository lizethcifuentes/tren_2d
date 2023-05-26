from tkinter import*

#-----------------
#variables globales
#------------------

BASE=480
ALTURA=480

#----------------------
#ventana principal
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


#CIRCULO TREN
circ_11 = c.create_oval(130,ALTURA-8-50,BASE/2-40,ALTURA-172, fill="green")
#rectangulos

#dibujar rectangulo
rect_1 = c.create_rectangle(BASE/2-40,BASE/2+190,410,ALTURA-180,fill="pink", outline="blue")
rect_3 = c.create_rectangle(BASE/2+30,BASE/2-50,410,ALTURA-180,fill="lime green", outline="black")
rect_2 = c.create_rectangle(BASE/2+40,BASE/2-45,400,ALTURA-190, fill="cyan")
rect_4 = c.create_rectangle(BASE/2+20,BASE/2-70,420,ALTURA-290, fill="thistle")
rect_5 = c.create_rectangle(BASE/2+40,BASE/2-90,400,ALTURA-310, fill="red")
rect_6 = c.create_rectangle(BASE/2-60,BASE/2+80,200,ALTURA-70,fill="blue")
rect_7 = c.create_rectangle(BASE/2-80,BASE/2+70,185,ALTURA-60, fill="cyan")
rect_8 = c.create_rectangle(BASE/2-30,BASE/2+60,230,ALTURA-220,fill="green")
rect_9 = c.create_rectangle(BASE/2-40,BASE/2+30,240,ALTURA-230, fill="dark gray")
rect_10 = c.create_rectangle(BASE/2+80,BASE/2+180,400,ALTURA-40,fill="thistle")
#dibujar circulos
circ_4 = c.create_oval(BASE/2+45,200,BASE-85,ALTURA/2+45, fill="white")
circ_3 = c.create_oval(BASE/2+190,BASE/2+150,370,ALTURA-20, fill="white")
circ_2 = c.create_oval(BASE/2+110,BASE/2+150,290,ALTURA-20, fill="white")
circ_1 = c.create_oval(BASE/2-30,BASE/2+150,270,ALTURA-20, fill="white")
#circ_11 = c.create_oval(90,ALTURA-8-50,BASE/2-40,ALTURA-170, fill="green")
#rectangulos llantas
rect_10 = c.create_rectangle(BASE/2+90,BASE/2+180,390,ALTURA-40,fill="thistle")
rect_11 = c.create_rectangle(BASE/2+10,BASE/2+180,310,ALTURA-40,fill="thistle")


#cara
circ_12 = c.create_oval(BASE/2+60,220,BASE-150,ALTURA/2+10, fill="green")
circ_13 = c.create_oval(BASE/2+100,220,BASE-110,ALTURA/2+10, fill="green")
line_b = c.create_line(BASE/2+125,270,BASE/2+72,ALTURA/2+30, fill="green",width=5)

#nombre
nom_l = c.create_text(BASE/2+70,ALTURA/2+90, anchor="center", text="lizeth cifuentes",font=("Arial",20, "bold"), fill="red",
activefill="cyan")



#----------------------
# FRAME DE CONTROLES 
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=480)
frame_controles.place(x=10, y=480)


# DESPLEGAR VENTANA 
ventana_principal.mainloop()









