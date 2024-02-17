import tkinter as tk
from tkinter import messagebox
import random

class Ahorcado:
    def __init__(self, master):
        self.master = master
        self.master.title("Ahorcado")

        self.palabras = ["python", "programacion", "ahorcado", "juego", "tkinter"]
        self.palabra_secreta = ""
        self.palabra_mostrada = []
        self.intentos_restantes = 6

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="lightblue")
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.letra_var = tk.StringVar()
        self.letra_entry = tk.Entry(self.master, textvariable=self.letra_var, font=("Helvetica", 16), width=5)
        self.letra_entry.grid(row=1, column=0, padx=10, pady=10)

        self.intentar_button = tk.Button(self.master, text="Intentar", command=self.intentar, font=("Helvetica", 14), bg="green", fg="white")
        self.intentar_button.grid(row=1, column=1, padx=10, pady=10)

        self.info_label = tk.Label(self.master, text="Intentos restantes: 6", font=("Helvetica", 12), fg="blue")
        self.info_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.iniciar_juego()  # Llamar a iniciar_juego después de crear el canvas

    def iniciar_juego(self):
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_mostrada = ["_"] * len(self.palabra_secreta)
        self.intentos_restantes = 6
        self.dibujar_ahorcado()

    def intentar(self):
        letra = self.letra_var.get().lower()
        if letra.isalpha() and len(letra) == 1:
            if letra in self.palabra_secreta:
                for i in range(len(self.palabra_secreta)):
                    if self.palabra_secreta[i] == letra:
                        self.palabra_mostrada[i] = letra
                if "_" not in self.palabra_mostrada:
                    self.mostrar_mensaje("¡Ganaste!", "Felicidades, has adivinado la palabra.")
                    self.iniciar_juego()
                else:
                    self.dibujar_ahorcado()
            else:
                self.intentos_restantes -= 1
                if self.intentos_restantes == 0:
                    self.mostrar_mensaje("Perdiste", f"La palabra era: {self.palabra_secreta}")
                    self.iniciar_juego()
                else:
                    self.dibujar_ahorcado()
        else:
            self.mostrar_mensaje("Error", "Ingresa una letra válida.")
        self.letra_var.set("")
        self.actualizar_interfaz()

    def dibujar_ahorcado(self):
        self.canvas.delete("all")
        self.canvas.create_line(50, 350, 350, 350, width=2)  # Base
        self.canvas.create_line(100, 350, 100, 50, width=2)   # Poste vertical
        self.canvas.create_line(100, 50, 250, 50, width=2)    # Travesaño
        self.canvas.create_line(250, 50, 250, 100, width=2)   # Cabeza

        if self.intentos_restantes < 6:
            self.canvas.create_oval(225, 100, 275, 150, width=2)  # Cabeza
        if self.intentos_restantes < 5:
            self.canvas.create_line(250, 150, 250, 250, width=2)  # Cuerpo
        if self.intentos_restantes < 4:
            self.canvas.create_line(250, 170, 230, 130, width=2)  # Brazo izquierdo
        if self.intentos_restantes < 3:
            self.canvas.create_line(250, 170, 270, 130, width=2)  # Brazo derecho
        if self.intentos_restantes < 2:
            self.canvas.create_line(250, 250, 230, 300, width=2)  # Pierna izquierda
        if self.intentos_restantes < 1:
            self.canvas.create_line(250, 250, 270, 300, width=2)  # Pierna derecha

        palabra_actual = " ".join(self.palabra_mostrada)
        self.canvas.create_text(200, 200, text=palabra_actual, font=("Helvetica", 18), fill="purple")

        self.info_label.config(text=f"Intentos restantes: {self.intentos_restantes}")

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def actualizar_interfaz(self):
        palabra_actual = " ".join(self.palabra_mostrada)
        self.canvas.create_text(200, 200, text=palabra_actual, font=("Helvetica", 18), fill="purple")

if __name__ == "__main__":
    root = tk.Tk()
    app = Ahorcado(root)
    root.mainloop()
