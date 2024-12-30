from Vista import *
from tkinter import *
from tkinter import messagebox
import sqlite3 

# Menu  BBDD Conectar-Crear "BaseUsuarios"
def Conectar():
    miConexion=sqlite3.connect("BaseUsuarios")
    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute('''CREATE TABLE Usuarios (IDEntry INTEGER PRIMARY KEY AUTOINCREMENT, 
                        NombreEntry VARCHAR(20), 
                        ApellidoEntry VARCHAR(20), 
                        ContraseñaEntry VARCHAR(20), 
                        NumeroEntry INTEGUER(9), 
                        ComentarioEntry VARCHAR(200))''')

        messagebox.showinfo("Informacion","Se ha creado y conectado a la base de datos")

    except:
        messagebox.showinfo("Informacion","Se ha conectado a la base de datos")

# Menu  BBDD Salir del programa con alerta de confirmacion
def Salir():
    val=messagebox.askyesno(" Salir","Seguro que quiere salir?")
    if val==True:
        exit()

# Menu CRED Crear, inserta datos a la base
def Crear():
    
    '''Registro=[(NombreEntry),
            (ApellidoEntry),
            (ContraseñaEntry),
            (NumeroEntry),
            (ComentarioEntry)]

    miConexion.execute("INSERT TO Usuarior values(null,?,?,?,?,?),Registro")
    miConexion.commit()'''
    
# Menu CRED Leer, enseña la informacion en funcion del id

# Menu CRED Actualizar, reescribe un dato

# Menu CRED Eliminar, suprimir un registro

# Menu Borrar, limpia los entrys
def BorrarF():
 '''   IDEntry.delete(0, END)
    NombreEntry.delete(0, END)
    ApellidoEntry.delete(0, END)
    ContraseñaEntry.delete(0, END)
    NumeroEntry.delete(0, END)
    ComentarioEntry.delete(1.0, END)'''

# Menu Ayuda licencia, messagebox con licencia
def licencia():
    messagebox.showinfo("Formulario","Licencia GPU")

# Menu Ayuda licencia, messagebox con acercade
def Acercade():
    messagebox.showinfo("Formulario","Autor: Valentin Tigovan")


