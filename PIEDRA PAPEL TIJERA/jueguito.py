import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class PiedraPapelTijeras:
    def __init__(self, master):
        self.master = master
        self.master.title("Piedra, Papel, Tijeras")

        self.opciones = ["Piedra", "Papel", "Tijeras"]
        self.resultados = []

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
        eleccion_computadora = random.choice(self.opciones)

        resultado = self.obtener_resultado(eleccion_usuario, eleccion_computadora)

        mensaje = f"Elegiste {eleccion_usuario}\nLa computadora eligió {eleccion_computadora}\nResultado: {resultado}"

        self.resultados.append(mensaje)
        self.actualizar_resultados()

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
        self.resultado_texto.config(state=tk.NORMAL)
        self.resultado_texto.delete(1.0, tk.END)
        for resultado in self.resultados:
            self.resultado_texto.insert(tk.END, resultado + "\n")
        self.resultado_texto.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeras(root)
    root.mainloop()
