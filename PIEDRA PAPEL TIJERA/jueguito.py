import tkinter as tk  # Importa el módulo tkinter con el alias tk.
from tkinter import messagebox  # Importa la función messagebox del módulo tkinter.
import random  # Importa el módulo random para generar números aleatorios.
from PIL import Image, ImageTk  # Importa las clases Image y ImageTk del módulo PIL.

class PiedraPapelTijeras:
    def __init__(self, master):
        self.master = master
        self.master.title("Piedra, Papel, Tijeras")  # Establece el título de la ventana.

        self.opciones = ["Piedra", "Papel", "Tijeras"]  # Lista de opciones disponibles.
        self.resultados = []  # Lista para almacenar resultados de juegos anteriores.

        self.etiqueta = tk.Label(self.master, text="Elige una opción:", font=("Helvetica", 16, "bold"))
        self.etiqueta.pack(pady=20)

        self.boton_piedra = tk.Button(self.master, text="Piedra", command=lambda: self.jugar("Piedra"), font=("Helvetica", 14))
        self.boton_piedra.pack(side=tk.LEFT, padx=20)

        self.boton_papel = tk.Button(self.master, text="Papel", command=lambda: self.jugar("Papel"), font=("Helvetica", 14))
        self.boton_papel.pack(side=tk.LEFT, padx=20)

        self.boton_tijeras = tk.Button(self.master, text="Tijeras", command=lambda: self.jugar("Tijeras"), font=("Helvetica", 14))
        self.boton_tijeras.pack(side=tk.LEFT, padx=20)

        self.resultado_texto = tk.Text(self.master, height=4, width=30, font=("Helvetica", 14), state=tk.DISABLED)
        self.resultado_texto.pack(pady=20)

        self.actualizar_resultados()

    def jugar(self, eleccion_usuario):
        eleccion_computadora = random.choice(self.opciones)  # Obtiene una elección aleatoria de la computadora.

        resultado = self.obtener_resultado(eleccion_usuario, eleccion_computadora)

        mensaje = f"Elegiste {eleccion_usuario}\nLa computadora eligió {eleccion_computadora}\nResultado: {resultado}"

        self.resultados.append(mensaje)  # Agrega el mensaje del resultado a la lista.
        self.actualizar_resultados()  # Actualiza la visualización de los resultados.

    def obtener_resultado(self, eleccion_usuario, eleccion_computadora):
        if eleccion_usuario == eleccion_computadora:
            return "Empate"
        elif (
            (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijeras") or
            (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or
            (eleccion_usuario == "Tijeras" and eleccion_computadora == "Papel")
        ):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

    def actualizar_resultados(self):
        self.resultado_texto.config(state=tk.NORMAL)  # Configura el estado del texto como normal para editar.
        self.resultado_texto.delete(1.0, tk.END)  # Borra el contenido actual del texto.
        for resultado in self.resultados:
            self.resultado_texto.insert(tk.END, resultado + "\n")  # Inserta cada resultado en el texto.
        self.resultado_texto.config(state=tk.DISABLED)  # Configura el estado del texto como deshabilitado.

if __name__ == "__main__":
    root = tk.Tk()  # Crea la instancia principal de Tkinter.
    app = PiedraPapelTijeras(root)  # Crea una instancia de la aplicación PiedraPapelTijeras.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
