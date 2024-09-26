import tkinter as tk
from tkinter import messagebox
import os

def guardar_datos():
    nombre = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()
    genero_valor = var_genero.get()

    if not nombre or not apellidos or not estatura or not telefono or genero_valor == 0:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    if not nombre.replace(" ", "").isalpha():
        messagebox.showerror("Error", "El nombre debe contener solo letras.")
        return

    if not apellidos.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Los apellidos deben contener solo letras.")
        return

    if not estatura.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "La estatura debe ser un numero valido.")
        return

    if not telefono.isdigit():
        messagebox.showerror("Error", "El telefono debe contener solo numeros.")
        return

    genero = "Masculino" if genero_valor == 1 else "Femenino"
    datos_completos = f"Nombre: {nombre} {apellidos} ({estatura} cm) - Telefono: {telefono} - Genero: {genero}"


    guardar_en_archivo(datos_completos)
    mostrar_datos_ventana(datos_completos)

def guardar_en_archivo(datos):
    carpeta = "C:\\Visual"
    archivo = os.path.join(carpeta, "datos_usuario.txt")
    try:
        with open(archivo, "a", encoding="utf-8") as file:
            file.write(datos + "\n")
        messagebox.showinfo("Guardado", f"Datos guardados en {archivo}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"La carpeta {carpeta} no existe. Crea la carpeta manualmente.")

def mostrar_datos_ventana(datos):
    ventana_datos = tk.Toplevel(Ventana)
    ventana_datos.title("Datos Ingresados")
    ventana_datos.geometry("400x200")

    lblMostrarDatos = tk.Label(ventana_datos, text=datos, wraplength=380)
    lblMostrarDatos.pack(pady=20)

    btnCerrar = tk.Button(ventana_datos, text="Cerrar", command=ventana_datos.destroy)
    btnCerrar.pack(pady=10)

Ventana = tk.Tk()
Ventana.title("Formulario de Usuarios")
Ventana.geometry("720x500")

lbNombre = tk.Label(Ventana, text="Nombre")
lbNombre.pack()

tbNombre = tk.Entry(Ventana)
tbNombre.pack()

lbApellidos = tk.Label(Ventana, text="Apellidos")
lbApellidos.pack()

tbApellidos = tk.Entry(Ventana)
tbApellidos.pack()

lbEstatura = tk.Label(Ventana, text="Estatura (cm)")
lbEstatura.pack()

tbEstatura = tk.Entry(Ventana)
tbEstatura.pack()

lbTelefono = tk.Label(Ventana, text="Telefono")
lbTelefono.pack()

tbTelefono = tk.Entry(Ventana)
tbTelefono.pack()

var_genero = tk.IntVar(value=0)
rbMasculino = tk.Radiobutton(Ventana, text="Masculino", variable=var_genero, value=1)
rbMasculino.pack()

rbFemenino = tk.Radiobutton(Ventana, text="Femenino", variable=var_genero, value=2)
rbFemenino.pack()

btnGuardar = tk.Button(Ventana, text="Guardar", command=guardar_datos)
btnGuardar.pack()

Ventana.mainloop()
