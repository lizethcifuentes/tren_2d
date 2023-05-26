from tkinter import*

#-----------------
#variables globales
#------------------

BASE=480
ALTURA=480

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

#triangulo base
polig_1= c.create_polygon(BASE/2,ALTURA/2,BASE-120,ALTURA,BASE/2-90,ALTURA,fill="thistle")

#arcos

arco_1 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=90, extent=45, fill="red")
arco_2 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=270, extent=45, fill="red")
arco_3 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=180, extent=45, fill="red")
arco_4 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=360, extent=45, fill="red")


#rectangulo
rec_1 = c.create_rectangle(BASE/2-100,BASE/2+200,360,ALTURA-20, fill="cyan")
 
#----------------------
# FRAME DE CONTROLES 
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=480)
frame_controles.place(x=10, y=480)


# DESPLEGAR VENTANA 
ventana_principal.mainloop()




