import customtkinter as ctk
import tkinterDnD
import secrets
import string
from tkinter import messagebox
import os

def guardar_contraseña():
    contraseña = entry_contraseña.get()
    if not contraseña:
        messagebox.showwarning("Advertencia", "Primero genera una contraseña antes de intentar guardar.")
        return
    
    try:
        nombre_archivo = "contraseñas_guardadas.txt"
        with open(nombre_archivo, "a") as archivo:
            archivo.write(contraseña + "\n")
        
        messagebox.showinfo("Éxito", "Contraseña guardada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al intentar guardar la contraseña:\n{str(e)}")
        
def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if not (8 <= longitud <= 24):
            raise ValueError("La longitud debe estar entre 8 y 24 caracteres.")
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña_generada = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        
        entry_contraseña.configure(state="normal")
        entry_contraseña.delete(0, "end")
        entry_contraseña.insert("end", contraseña_generada)
        entry_contraseña.configure(state="readonly")
    except ValueError as e:
        messagebox.showerror("Error", "Ingresa una longitud válida para la contraseña (entre 8 y 24 caracteres enteros).")

ctk.set_ctk_parent_class(tkinterDnD.Tk)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Generador de Contraseñas")

frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)

label_titulo = ctk.CTkLabel(frame_principal, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=10)

label_longitud = ctk.CTkLabel(frame_principal, text="Longitud de la Contraseña (8-24):")
label_longitud.pack(pady=5)

entry_longitud = ctk.CTkEntry(frame_principal)
entry_longitud.pack(pady=10)

label_contraseña = ctk.CTkLabel(frame_principal, text="Contraseña Generada:")
label_contraseña.pack(pady=5)

entry_contraseña = ctk.CTkEntry(frame_principal, state="readonly")
entry_contraseña.pack(pady=10)

button_generar = ctk.CTkButton(frame_principal, text="Generar Contraseña", command=generar_contraseña)
button_generar.pack(pady=10)

button_guardar = ctk.CTkButton(frame_principal, text="Guardar Contraseña", command=guardar_contraseña)
button_guardar.pack(pady=10)

app.mainloop()
