import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def nuevo_archivo():
    text_area.delete(1.0, tk.END)
    actualizar_contador_palabras()

def abrir_archivo():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
                actualizar_contador_palabras()
        except Exception as e:
            mostrar_error("Error", f"No se pudo abrir el archivo: {e}")

def guardar_archivo():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        try:
            content = text_area.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            mostrar_error("Error", f"No se pudo guardar el archivo: {e}")

def salir():
    root.destroy()

def mostrar_error(titulo, mensaje):
    messagebox.showerror(titulo, mensaje)

def actualizar_contador_palabras():
    contenido = text_area.get(1.0, tk.END)
    palabras = contenido.split(None)  # Utilizar split(None) para contar todas las palabras
    contador_palabras.set(f"Palabras: {len(palabras)}")

root = tk.Tk()
root.title("Bloc de notas")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_area.pack(expand=True, fill='both')

contador_palabras = tk.StringVar()
label_contador_palabras = tk.Label(root, textvariable=contador_palabras)
label_contador_palabras.pack(side=tk.BOTTOM)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

file_menu.add_command(label="Nuevo", command=nuevo_archivo)
file_menu.add_command(label="Abrir", command=abrir_archivo)
file_menu.add_command(label="Guardar", command=guardar_archivo)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=salir)

root.mainloop()
