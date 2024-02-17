import customtkinter as ctk  # Importa el módulo customtkinter con el alias ctk.
import tkinterDnD  # Importa el módulo tkinterDnD.
import secrets  # Importa el módulo secrets para la generación segura de contraseñas.
import string  # Importa el módulo string para trabajar con caracteres.
from tkinter import filedialog  # Importa la función filedialog del módulo tkinter.
from tkinter import messagebox  # Importa la función messagebox del módulo tkinter.
import os  # Importa el módulo os para interactuar con el sistema operativo.

def guardar_contraseña():
    # Obtiene la contraseña del cuadro de entrada
    contraseña = entry_contraseña.get()
    # Verifica si la contraseña está vacía
    if not contraseña:
        messagebox.showwarning("Advertencia", "Primero genera una contraseña antes de intentar guardar.")
        return
    
    try:
        # Seleccionar la ubicación y el nombre del archivo usando un cuadro de diálogo
        nombre_archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
            title="Guardar Contraseña"
        )
        
        # Verifica si el usuario canceló la operación
        if not nombre_archivo:
            return
        
        # Abre el archivo en modo de añadir y escribe la contraseña seguida de un salto de línea
        with open(nombre_archivo, "a") as archivo:
            archivo.write(contraseña + "\n")
        
        messagebox.showinfo("Éxito", "Contraseña guardada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al intentar guardar la contraseña:\n{str(e)}")

def generar_contraseña():
    try:
        # Obtiene la longitud de la contraseña desde el cuadro de entrada
        longitud = int(entry_longitud.get())
        # Verifica que la longitud esté dentro del rango especificado
        if not (8 <= longitud <= 24):
            raise ValueError("La longitud debe estar entre 8 y 24 caracteres.")
        
        # Define los caracteres posibles para la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Genera la contraseña aleatoria utilizando secrets.choice
        contraseña_generada = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        
        # Configura el cuadro de entrada de la contraseña para permitir modificaciones
        entry_contraseña.configure(state="normal")
        # Borra cualquier contenido previo del cuadro de entrada
        entry_contraseña.delete(0, "end")
        # Inserta la contraseña generada en el cuadro de entrada
        entry_contraseña.insert("end", contraseña_generada)
        # Configura el cuadro de entrada de la contraseña como solo lectura
        entry_contraseña.configure(state="readonly")
    except ValueError as e:
        messagebox.showerror("Error", "Ingresa una longitud válida para la contraseña (entre 8 y 24 caracteres enteros).")

ctk.set_ctk_parent_class(tkinterDnD.Tk)  # Establece la clase principal de customtkinter para arrastrar y soltar.
ctk.set_appearance_mode("dark")  # Establece el modo de apariencia en "dark".
ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado en "blue".

app = ctk.CTk()  # Crea una instancia de la clase CTk de customtkinter.
app.geometry("400x400")  # Establece las dimensiones de la ventana.
app.title("Generador de Contraseñas")  # Establece el título de la ventana.

frame_principal = ctk.CTkFrame(app)  # Crea un marco principal utilizando la clase CTkFrame.
frame_principal.pack(fill="both", expand=True)  # Empaqueta el marco principal para llenar y expandirse.

label_titulo = ctk.CTkLabel(frame_principal, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=10)  # Empaqueta la etiqueta del título con un espacio vertical de 10 píxeles.

label_longitud = ctk.CTkLabel(frame_principal, text="Longitud de la Contraseña (8-24):")
label_longitud.pack(pady=5)  # Empaqueta la etiqueta de longitud con un espacio vertical de 5 píxeles.

entry_longitud = ctk.CTkEntry(frame_principal)  # Crea un cuadro de entrada para la longitud de la contraseña.
entry_longitud.pack(pady=10)  # Empaqueta el cuadro de entrada de longitud con un espacio vertical de 10 píxeles.

label_contraseña = ctk.CTkLabel(frame_principal, text="Contraseña Generada:")
label_contraseña.pack(pady=5)  # Empaqueta la etiqueta de la contraseña con un espacio vertical de 5 píxeles.

entry_contraseña = ctk.CTkEntry(frame_principal, state="readonly")  # Crea un cuadro de entrada para la contraseña con estado de solo lectura.
entry_contraseña.pack(pady=10)  # Empaqueta el cuadro de entrada de la contraseña con un espacio vertical de 10 píxeles.

button_generar = ctk.CTkButton(frame_principal, text="Generar Contraseña", command=generar_contraseña)
button_generar.pack(pady=10)  # Empaqueta el botón de generación de contraseña con un espacio vertical de 10 píxeles.

button_guardar = ctk.CTkButton(frame_principal, text="Guardar Contraseña", command=guardar_contraseña)
button_guardar.pack(pady=10)  # Empaqueta el botón de guardado de contraseña con un espacio vertical de 10 píxeles.

app.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
