import tkinter as tk  # Importa la biblioteca tkinter con el alias 'tk'.
from tkinter import messagebox  # Importa la clase 'messagebox' de tkinter.
import random  # Importa la biblioteca random para generar palabras aleatorias.

class Ahorcado:
    def __init__(self, master):
        self.master = master  # Inicializa la ventana principal.
        self.master.title("Ahorcado")  # Establece el título de la ventana.

        self.palabras = ["python", "paraplegico", "ahorcado", "juego", "tkinter"]  # Lista de palabras posibles.
        self.palabra_secreta = ""  # Inicializa la palabra secreta.
        self.palabra_mostrada = []  # Inicializa la lista de letras mostradas.
        self.intentos_restantes = 6  # Número de intentos permitidos.

        # Configuración del lienzo (canvas) en la ventana.
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="lightblue")
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Configuración del Entry para ingresar letras.
        self.letra_var = tk.StringVar()
        self.letra_entry = tk.Entry(self.master, textvariable=self.letra_var, font=("Helvetica", 16), width=5)
        self.letra_entry.grid(row=1, column=0, padx=10, pady=10)

        # Configuración del botón para intentar adivinar la letra.
        self.intentar_button = tk.Button(self.master, text="Intentar", command=self.intentar, font=("Helvetica", 14), bg="green", fg="white")
        self.intentar_button.grid(row=1, column=1, padx=10, pady=10)

        # Configuración de la etiqueta para mostrar la información de los intentos restantes.
        self.info_label = tk.Label(self.master, text="Intentos restantes: 6", font=("Helvetica", 12), fg="blue")
        self.info_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.iniciar_juego()  # Llama al método iniciar_juego después de crear el canvas.

    def iniciar_juego(self):
        # Inicializa la palabra secreta, la lista de letras mostradas y los intentos restantes.
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_mostrada = ["_"] * len(self.palabra_secreta)
        self.intentos_restantes = 6
        self.dibujar_ahorcado()  # Llama al método dibujar_ahorcado para actualizar la representación gráfica.

    def intentar(self):
        letra = self.letra_var.get().lower()  # Obtiene la letra ingresada en minúsculas.
        if letra.isalpha() and len(letra) == 1:  # Verifica que la entrada sea una letra única.
            if letra in self.palabra_secreta:  # Comprueba si la letra está en la palabra secreta.
                # Actualiza la lista de letras mostradas.
                for i in range(len(self.palabra_secreta)):
                    if self.palabra_secreta[i] == letra:
                        self.palabra_mostrada[i] = letra
                if "_" not in self.palabra_mostrada:  # Si no hay letras ocultas, el jugador ha ganado.
                    self.mostrar_mensaje("¡Ganaste!", "Felicidades, has adivinado la palabra.")
                    self.iniciar_juego()  # Reinicia el juego después de mostrar el mensaje de victoria.
                else:
                    self.dibujar_ahorcado()  # Actualiza la representación gráfica.
            else:
                self.intentos_restantes -= 1  # Reduce el número de intentos restantes.
                if self.intentos_restantes == 0:
                    self.mostrar_mensaje("Perdiste", f"La palabra era: {self.palabra_secreta}")
                    self.iniciar_juego()  # Reinicia el juego después de mostrar el mensaje de derrota.
                else:
                    self.dibujar_ahorcado()  # Actualiza la representación gráfica.
        else:
            self.mostrar_mensaje("Error", "Ingresa una letra válida.")
        self.letra_var.set("")  # Limpia la entrada de letras.
        self.actualizar_interfaz()  # Actualiza la interfaz gráfica.

    def dibujar_ahorcado(self):
        # Borra todos los elementos en el lienzo.
        self.canvas.delete("all")
        # Dibuja los elementos del ahorcado según los intentos restantes.
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

        # Muestra la palabra actual en el lienzo.
        palabra_actual = " ".join(self.palabra_mostrada)
        self.canvas.create_text(200, 200, text=palabra_actual, font=("Helvetica", 18), fill="purple")

        # Actualiza la etiqueta de información de intentos restantes.
        self.info_label.config(text=f"Intentos restantes: {self.intentos_restantes}")

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)  # Muestra un cuadro de mensaje.

    def actualizar_interfaz(self):
        # Actualiza la representación gráfica de la palabra actual.
        palabra_actual = " ".join(self.palabra_mostrada)
        self.canvas.create_text(200, 200, text=palabra_actual, font=("Helvetica", 18), fill="purple")

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal.
    app = Ahorcado(root)  # Crea una instancia de la clase Ahorcado.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
