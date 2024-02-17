import tkinter as tk  # Importa la biblioteca tkinter con el alias 'tk'.
from tkinter import scrolledtext, filedialog, messagebox  # Importa clases específicas de tkinter.

def nuevo_archivo():
    text_area.delete(1.0, tk.END)  # Elimina todo el contenido del área de texto.
    actualizar_contador_palabras()

def abrir_archivo():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)  # Limpia el área de texto.
                text_area.insert(tk.END, content)  # Inserta el contenido del archivo en el área de texto.
                actualizar_contador_palabras()
        except Exception as e:
            mostrar_error("Error", f"No se pudo abrir el archivo: {e}")

def guardar_archivo():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        try:
            content = text_area.get(1.0, tk.END)  # Obtiene todo el contenido del área de texto.
            with open(file_path, 'w') as file:
                file.write(content)  # Escribe el contenido en el archivo.
        except Exception as e:
            mostrar_error("Error", f"No se pudo guardar el archivo: {e}")

def salir():
    root.destroy()  # Cierra la ventana principal.

def mostrar_error(titulo, mensaje):
    messagebox.showerror(titulo, mensaje)  # Muestra un cuadro de mensaje de error.

def actualizar_contador_palabras():
    contenido = text_area.get(1.0, tk.END)  # Obtiene todo el contenido del área de texto.
    palabras = contenido.split(None)  # Divide el contenido en palabras utilizando espacios en blanco.
    contador_palabras.set(f"Palabras: {len(palabras)}")  # Actualiza el contador de palabras.

root = tk.Tk()  # Crea la ventana principal.
root.title("Bloc de notas")  # Establece el título de la ventana.

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)  # Crea un área de texto desplazable.
text_area.pack(expand=True, fill='both')  # Empaqueta y expande el área de texto.

contador_palabras = tk.StringVar()  # Variable para el contador de palabras.
label_contador_palabras = tk.Label(root, textvariable=contador_palabras)  # Etiqueta para mostrar el contador.
label_contador_palabras.pack(side=tk.BOTTOM)  # Empaqueta la etiqueta en la parte inferior.

menu_bar = tk.Menu(root)  # Barra de menú principal.
root.config(menu=menu_bar)  # Configura la barra de menú.

file_menu = tk.Menu(menu_bar, tearoff=0)  # Menú desplegable de archivo.
menu_bar.add_cascade(label="Archivo", menu=file_menu)  # Agrega el menú desplegable a la barra de menú.

file_menu.add_command(label="Nuevo", command=nuevo_archivo)  # Agrega la opción "Nuevo" al menú de archivo.
file_menu.add_command(label="Abrir", command=abrir_archivo)  # Agrega la opción "Abrir" al menú de archivo.
file_menu.add_command(label="Guardar", command=guardar_archivo)  # Agrega la opción "Guardar" al menú de archivo.
file_menu.add_separator()  # Agrega un separador en el menú de archivo.
file_menu.add_command(label="Salir", command=salir)  # Agrega la opción "Salir" al menú de archivo.

root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
