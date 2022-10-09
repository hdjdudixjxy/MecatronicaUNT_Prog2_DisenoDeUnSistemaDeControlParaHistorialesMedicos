import tkinter as tk
from tkinter import messagebox

############ CLASE TK ###############

aplicacion=tk.Tk()

aplicacion.title("OPERACIONES MÉDICAS")
aplicacion.geometry("480x790+1030+15") 
aplicacion.resizable(0,0)
aplicacion.iconbitmap("icon.ico")
aplicacion.configure(background="bisque2") 

################ CLASES FRAME ###############

ventana1=tk.Frame(aplicacion)
ventana1.configure(bg="bisque2",height=150)

ventana2=tk.LabelFrame(aplicacion)
ventana2.configure(text="Eliga la operación", font=("Verdana", 15, "bold"), border=5, bg="bisque4")

subventana1=tk.Frame(ventana2, bg="bisque4")
subventana2=tk.Frame(ventana2, bg="bisque4")

########## CLASES ENTRYS ################

operacion=tk.StringVar()

entry=tk.Entry(ventana1)
entry.configure(textvariable=operacion, font=("Verdana", 15), bg="bisque4", selectbackground="bisque3")

precio=tk.IntVar()

entry2=tk.Entry(ventana1)
entry2.configure(textvariable=precio, font=("Verdana", 15), bg="bisque4", selectbackground="bisque3")

########## CLASES LABELS ############

etiqueta1=tk.Label(ventana1)
etiqueta1.configure(text="Operación a agregar", font=("Verdana", 15, "underline", "bold"),bg="bisque2")

etiqueta2=tk.Label(ventana1)
etiqueta2.configure(text="Monto a pagar", font=("Verdana", 15, "underline", "bold"),bg="bisque2")

################ CLASE LISTBOX #####################

lista=tk.Listbox(subventana1)
lista.configure(bg="bisque3", selectbackground="navajowhite3", selectforeground="black", width=28, height=15,
                font=("Verdana", 15), cursor="hand2", justify=tk.LEFT, selectborderwidth=4, selectmode=tk.EXTENDED)

diccionario_operaciones={"Reducción abierta de fractura con fijación interna":"2000 soles","Laparotomía exploradora":"3000 soles", 
"Herniorrafia umbilical abierta":"3215 soles","Reparación unilateral de hernia":"325 soles","Apendicectomía":"3025 soles","Incisión de tejido subcutáneo":"525 soles",
"Extirpación local":"2325 soles","Sustitución de derivación ventricular":"3225 soles","Reducción abierta de fractura":"1325 soles"}

lista.insert(0,*diccionario_operaciones)

def agregar_datos():

    """Función para insertar las operaciones y el precio"""

    Operacion=operacion.get()
    Precio=precio.get()
    
    try:
        if Operacion in diccionario_operaciones:
            pass
        elif Operacion=="":
            titulo = "Agregar operación"
            mensaje = "Error al agregar operación"
            messagebox.showerror(titulo, mensaje)
        else:
            diccionario_operaciones[Operacion]=f"{Precio} soles"
            lista.insert(tk.END,Operacion)

    except:
        titulo = "Agregar operación"
        mensaje = "Error al agregar operación"
        messagebox.showerror(titulo, mensaje)
            

def eliminar_datos():

    """Función para eliminar datos del diccionario operaciones"""

    #a=list(range(int(lista.size)))
    #print(a[1])
    tupla=(lista.curselection())

    try:

        del(diccionario_operaciones[lista.get(tupla[0])])
        lista.delete(tupla[0])
        print(diccionario_operaciones)

    except:
        titulo = "Eliminar operación"
        mensaje = "Error al eliminar la operación"
        messagebox.showerror(titulo, mensaje)

def insertar_datos():

    """Función para insertar las operaciones y el precio"""

    pass

########## CLASES BUTTON #############

boton1=tk.Button(ventana1)
boton1.configure(text="AGREGAR", bg="orangered3", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="orangered4", command=agregar_datos)

boton2=tk.Button(ventana1)
boton2.configure(text="ELIMINAR", bg="orangered3", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="orangered4", command=eliminar_datos)

boton3=tk.Button(aplicacion)
boton3.configure(text="INSERTAR", bg="orangered3", cursor="hand2", font=("Verdana", 13, "bold"), activebackground="orangered4", width=28)


scrollbar1 = tk.Scrollbar(subventana2) 
scrollbar1.configure(orient="vertical", command = lista.yview) 
lista.configure(yscrollcommand = scrollbar1.set) 
  


scrollbar2 = tk.Scrollbar(subventana1)
scrollbar2.configure(orient="horizontal", command = lista.xview) 

lista.config(xscrollcommand = scrollbar2.set) 
  


ventana1.pack(fill=tk.X)
ventana2.pack(padx=10,pady=10)
entry.place(x=40,y=36)
entry2.place(x=40,y=104)
boton1.place(x=325,y=34)
boton2.place(x=325,y=102)
etiqueta1.place(x=40,y=0)
etiqueta2.place(x=40,y=66)
boton3.pack(pady=6)
subventana1.pack(side = tk.LEFT, fill = tk.BOTH)
subventana2.pack(side = tk.RIGHT, fill = tk.BOTH)
lista.pack()
scrollbar1.pack(side = tk.RIGHT, fill = tk.BOTH)
scrollbar2.pack(side = tk.BOTTOM, fill = tk.BOTH)

aplicacion.mainloop()

