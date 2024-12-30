#Importacion de librerias necesarias
from tkinter import *
from tkinter import messagebox
import sqlite3

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

global miConexion
global miCursor

miConexion=sqlite3.connect("BaseUsuarios")
miCursor=miConexion.cursor()

# Menu  BBDD Conectar-Crear "BaseUsuarios"
def Conectar():

    try:
        miCursor.execute('''CREATE TABLE Usuarios (IDEntry INTEGER PRIMARY KEY AUTOINCREMENT, 
                            NombreEntry VARCHAR(20), 
                            ApellidoEntry VARCHAR(20), 
                            ContraseñaEntry VARCHAR(20), 
                            NumeroEntry INTEGER(9), 
                            ComentarioEntry VARCHAR(200))''')
        
        messagebox.showinfo("","Se ha creado la base de datos")
    except:
        messagebox.showinfo("","Se ha conectado a la base de datos")

BBDD.add_command(label="Conectar", command=Conectar)

# Menu  BBDD Salir del programa con alerta de confirmacion
def Salir():
    val=messagebox.askyesno(" Salir","Seguro que quiere salir?")
    if val==True:
        exit()

BBDD.add_command(label="Salir", command=Salir)
    
# Menu CRED
BarraMenu.add_cascade(label="CRED", menu= CRED)
# Menu CRED Crear, inserta datos a la base
def Crear():

    Registro=(Entry.get(NombreEntry),
            Entry.get(ApellidoEntry),
            Entry.get(ContraseñaEntry),
            Entry.get(NumeroEntry))

    print(Registro)

    
    miCursor.execute("INSERT INTO Usuarios VALUES(NULL,?,?,?,?,NULL)", Registro)

    miConexion.commit()

CRED.add_command(label="Crear", command=Crear)
# Menu CRED Leer, enseña la informacion en funcion del id
def Leer():
    ID=Entry.get(IDEntry)

    miCursor.execute("SELECT * FROM Usuarios WHERE  IDEntry="+ID)

    FilaTupla=miCursor.fetchall()
    FilaLista=FilaTupla[0]

    BorrarF()

    IDEntry.insert(0,FilaLista[0])
    NombreEntry.insert(0,FilaLista[1])
    ApellidoEntry.insert(0,FilaLista[2])
    ContraseñaEntry.insert(0, FilaLista[3])
    NumeroEntry.insert(0,FilaLista[4])
    ComentarioEntry.insert(0,FilaLista[5])

    miConexion.commit()

CRED.add_command(label="Leer", command=Leer)
# Menu CRED Actualizar, reescribe un dato
def Actualizar():

    ID=Entry.get(IDEntry)

    Registro=(Entry.get(NombreEntry),
            Entry.get(ApellidoEntry),
            Entry.get(ContraseñaEntry),
            Entry.get(NumeroEntry))
    print("UPDATE Usuarios SET NombreEntry='"+Entry.get(NombreEntry)+"',ApellidoEntry='"+Entry.get(ApellidoEntry)+"',ContraseñaEntry='"+Entry.get(ContraseñaEntry)+"',NumeroEntry="+Entry.get(NumeroEntry)+" WHERE  IDEntry="+ID)
    miCursor.execute("UPDATE Usuarios SET NombreEntry='"+Entry.get(NombreEntry)+"',ApellidoEntry='"+Entry.get(ApellidoEntry)+"',ContraseñaEntry='"+Entry.get(ContraseñaEntry)+"',NumeroEntry="+Entry.get(NumeroEntry)+" WHERE  IDEntry="+ID)

    miConexion.commit()

CRED.add_command(label="Actualizar", command=Actualizar)
# Menu CRED Eliminar, suprimir un registro

def Eliminar():
    ID=Entry.get(IDEntry)
    miCursor.execute("DELETE FROM Usuarios WHERE  IDEntry="+ID)

    miConexion.commit()

CRED.add_command(label="Eliminar")

# Menu Borrar
BarraMenu.add_cascade(label="Borrar", menu= Borrar)

def BorrarF():
    IDEntry.delete(0, END)
    NombreEntry.delete(0, END)
    ApellidoEntry.delete(0, END)
    ContraseñaEntry.delete(0, END)
    NumeroEntry.delete(0, END)
    ComentarioEntry.delete(1.0, END)
    
    miConexion.commit()

Borrar.add_command(label="Borrar Campos", command= BorrarF)

# Menu Ayuda
BarraMenu.add_cascade(label="Ayuda", menu= Ayuda)

def licencia():
    messagebox.showinfo("Formulario","Licencia GPU")

Ayuda.add_command(label="Licencia", command=licencia)

def Acercade():
    messagebox.showinfo("Formulario","Autor: Valentin Tigovan")

Ayuda.add_command(label="Acerca del programa",command=Acercade)

# Texto
Label(raiz, text="ID").grid(row = 1, column = 0, padx=20, pady=10)
Label(raiz, text="Nombre").grid(row = 2, column = 0, padx=20, pady=10)
Label(raiz, text="Apellido").grid(row = 3, column = 0, padx=20, pady=10)
Label(raiz, text="Contraseña").grid(row = 4, column = 0, padx=20, pady=10)
Label(raiz, text="Numero").grid(row = 5, column = 0, padx=20, pady=10)
Label(raiz, text="Comentario").grid(row = 6, column = 0, padx=20, pady=10)

# Entradas
IDEntry=IntVar()
IDEntry=Entry(raiz) 
IDEntry.grid(row = 1, column = 2, padx=20, pady=10)
NombreEntry=Entry(raiz)
NombreEntry.grid(row = 2, column = 2, padx=20, pady=10)
ApellidoEntry=Entry(raiz)
ApellidoEntry.grid(row = 3, column = 2, padx=20, pady=10)
ContraseñaEntry=Entry(raiz)
ContraseñaEntry.grid(row = 4, column = 2, padx=20, pady=10)
ContraseñaEntry.config(show="*")
NumeroEntry=IntVar()
NumeroEntry=Entry(raiz)
NumeroEntry.grid(row = 5, column = 2, padx=20, pady=10)
ComentarioEntry=Text(raiz, width=15, height=5)
ComentarioEntry.grid(row = 6, column = 2, padx=20, pady=10)

#Botones
BotonCreate = Button(raiz, text="Create", width=10, command=Crear).grid(row = 2, column = 3, padx=20)
BotonRead = Button(raiz, text="Read", width=10,command=Leer).grid(row = 3, column = 3, padx=20)
BotonUpdate = Button(raiz, text="Update", width=10, command=Actualizar).grid(row = 4, column = 3, padx=20)
BotonDelete = Button(raiz, text="Delete", width=10, command=Eliminar).grid(row = 5, column = 3, padx=20)

raiz.mainloop()