from Modelo import *
from tkinter import *

#IDEntry, NombreEntry, ApellidoEntry, ContraseñaEntry, NumeroEntry, ComentarioEntry

Conectar()

raiz=Tk()

raiz.title("Formulario")
raiz.resizable(0,0)

#Construccion de la barra de menu
BarraMenu=Menu(raiz)
raiz.config(menu=BarraMenu)

BBDD=Menu(BarraMenu, tearoff=0)
Borrar=Menu(BarraMenu, tearoff=0)
CRED=Menu(BarraMenu, tearoff=0)
Ayuda=Menu(BarraMenu, tearoff=0)

# Menu  BBDD

BarraMenu.add_cascade(label="BBDD", menu= BBDD)

BBDD.add_command(label="Conectar", command=Conectar)
BBDD.add_command(label="Salir", command=Salir)
    
# Menu CRED
BarraMenu.add_cascade(label="CRED", menu= CRED)

CRED.add_command(label="Crear")
CRED.add_command(label="Leer")
CRED.add_command(label="Actualizar")
CRED.add_command(label="Eliminar")

# Menu Borrar
BarraMenu.add_cascade(label="Borrar", menu= Borrar)

Borrar.add_command(label="Borrar Campos", command= BorrarF)

# Menu Ayuda
BarraMenu.add_cascade(label="Ayuda", menu= Ayuda)

Ayuda.add_command(label="Licencia", command=licencia)
Ayuda.add_command(label="Acerca del programa",command=Acercade)

# Texto
Label(raiz, text="ID").grid(row = 1, column = 0, padx=20, pady=10)
Label(raiz, text="Nombre").grid(row = 2, column = 0, padx=20, pady=10)
Label(raiz, text="Apellido").grid(row = 3, column = 0, padx=20, pady=10)
Label(raiz, text="Contraseña").grid(row = 4, column = 0, padx=20, pady=10)
Label(raiz, text="Numero").grid(row = 5, column = 0, padx=20, pady=10)
Label(raiz, text="Comentario").grid(row = 6, column = 0, padx=20, pady=10)

# Entradas
IDEntry=Entry(raiz) 
IDEntry.grid(row = 1, column = 2, padx=20, pady=10)
NombreEntry=Entry(raiz)
NombreEntry.grid(row = 2, column = 2, padx=20, pady=10)
ApellidoEntry=Entry(raiz)
ApellidoEntry.grid(row = 3, column = 2, padx=20, pady=10)
ContraseñaEntry=Entry(raiz)
ContraseñaEntry.grid(row = 4, column = 2, padx=20, pady=10)
ContraseñaEntry.config(show="*")
NumeroEntry=Entry(raiz)
NumeroEntry.grid(row = 5, column = 2, padx=20, pady=10)
ComentarioEntry=Text(raiz, width=15, height=5)
ComentarioEntry.grid(row = 6, column = 2, padx=20, pady=10)

#Botones
BotonCreate = Button(raiz, text="Create", width=10).grid(row = 2, column = 3, padx=20)
BotonRead = Button(raiz, text="Read", width=10).grid(row = 3, column = 3, padx=20)
BotonUpdate = Button(raiz, text="Update", width=10).grid(row = 4, column = 3, padx=20)
BotonDelete = Button(raiz, text="Delete", width=10).grid(row = 5, column = 3, padx=20)

raiz.mainloop()