import customtkinter as ctk  # Importa el módulo customtkinter con el alias ctk.
from tkinter import messagebox  # Importa la función messagebox del módulo tkinter.
import tkinterDnD  # Importa el módulo tkinterDnD para arrastrar y soltar.

class CalculadoraImpuestosApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")  # Establece las dimensiones de la ventana.
        self.title("Calculadora de Impuestos")  # Establece el título de la ventana.

        self.frame_principal = ctk.CTkFrame(self)  # Crea un marco utilizando la clase CTkFrame.
        self.frame_principal.pack(fill="both", expand=True)  # Empaqueta el marco con expansión para llenar.

        self.label_titulo = ctk.CTkLabel(self.frame_principal, text="Calculadora de Impuestos", font=("Helvetica", 16, "bold"))
        self.label_titulo.pack(pady=10)  # Empaqueta la etiqueta de título con espaciado vertical de 10 píxeles.

        self.label_dolares = ctk.CTkLabel(self.frame_principal, text="Cantidad de dólares a pagar:")
        self.label_dolares.pack(pady=5)  # Empaqueta la etiqueta de dólares con espaciado vertical de 5 píxeles.

        self.entry_dolares = ctk.CTkEntry(self.frame_principal)
        self.entry_dolares.pack(pady=10)  # Empaqueta la entrada de dólares con espaciado vertical de 10 píxeles.

        self.label_resultado = ctk.CTkLabel(self.frame_principal, text="Resultado:")
        self.label_resultado.pack(pady=5)  # Empaqueta la etiqueta de resultado con espaciado vertical de 5 píxeles.

        self.button_calcular = ctk.CTkButton(self.frame_principal, text="Calcular Impuestos", command=self.calcular_impuestos)
        self.button_calcular.pack(pady=10)  # Empaqueta el botón de cálculo de impuestos con espaciado vertical de 10 píxeles.

    def calcular_impuestos(self):
        try:
            cantidad_dolares = float(self.entry_dolares.get())  # Obtiene la cantidad de dólares desde la entrada.

            cotizacion_oficial = 850.00  # Cotización del dólar oficial en ARS

            # Calcula el monto en pesos argentinos sin impuestos
            monto_sin_impuestos = cantidad_dolares * cotizacion_oficial

            # Calcula los impuestos PAIS (30%) y Ganancias (30%)
            impuesto_pais = monto_sin_impuestos * 0.30
            impuesto_ganancias = monto_sin_impuestos * 0.30

            # Calcula el monto total en pesos argentinos con impuestos
            monto_con_impuestos = monto_sin_impuestos + impuesto_pais + impuesto_ganancias

            resultado_texto = (
                f"PESOS (ARS) sin impuestos: {monto_sin_impuestos:.2f}\n"
                f"+ Impuesto PAÍS (30%): {impuesto_pais:.2f}\n"
                f"+ Imp. a las ganancias (30%): {impuesto_ganancias:.2f}\n"
                f"Cantidad de PESOS (ARS) con impuestos: {monto_con_impuestos:.2f}"
            )
            messagebox.showinfo("Resultado", resultado_texto)  # Muestra la información del resultado en un cuadro de diálogo.
        except ValueError:
            messagebox.showerror("Error", "Ingresa una cantidad válida de dólares.")

if __name__ == "__main__":
    ctk.set_ctk_parent_class(tkinterDnD.Tk)  # Establece la clase principal de customtkinter para arrastrar y soltar.
    ctk.set_appearance_mode("dark")  # Establece el modo de apariencia en "dark".
    ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado en "blue".

    app = CalculadoraImpuestosApp()  # Crea una instancia de la aplicación CalculadoraImpuestosApp.
    app.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
