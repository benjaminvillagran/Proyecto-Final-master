import customtkinter  # Importa el módulo customtkinter.
import tkinterDnD  # Importa el módulo tkinterDnD para arrastrar y soltar.
from tkinter import messagebox  # Importa la función messagebox del módulo tkinter.

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)  # Establece la clase principal de customtkinter para arrastrar y soltar.

customtkinter.set_appearance_mode("dark")  # Establece el modo de apariencia en "dark". Modos: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Establece el tema de color predeterminado en "blue". Temas: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()  # Crea una instancia de la clase CTk de customtkinter.
app.geometry("400x780")  # Establece las dimensiones de la ventana.
app.title("CustomTkinter IMC Calculator")  # Establece el título de la ventana.

frame_1 = customtkinter.CTkFrame(master=app)  # Crea un marco utilizando la clase CTkFrame.
frame_1.pack(pady=20, padx=60, fill="both", expand=True)  # Empaqueta el marco con espaciado vertical de 20 píxeles, espaciado horizontal de 60 píxeles, y se expande para llenar.

label_peso = customtkinter.CTkLabel(master=frame_1, text="Peso:")  # Crea una etiqueta para el peso.
label_peso.pack(pady=10, padx=10)  # Empaqueta la etiqueta de peso con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

slider_peso = customtkinter.CTkSlider(master=frame_1, from_=0, to=265, command=lambda value: actualizar_label_peso(value, label_peso_valor))  # Crea un control deslizante para el peso.
slider_peso.pack(pady=10, padx=10)  # Empaqueta el control deslizante de peso con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

label_peso_valor = customtkinter.CTkLabel(master=frame_1, text="Peso: 0 kg")  # Crea una etiqueta para mostrar el valor del peso.
label_peso_valor.pack(pady=10, padx=10)  # Empaqueta la etiqueta de valor de peso con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

label_altura = customtkinter.CTkLabel(master=frame_1, text="Altura:")  # Crea una etiqueta para la altura.
label_altura.pack(pady=10, padx=10)  # Empaqueta la etiqueta de altura con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

slider_altura = customtkinter.CTkSlider(master=frame_1, from_=0, to=2.5, command=lambda value: actualizar_label_altura(value, label_altura_valor))  # Crea un control deslizante para la altura.
slider_altura.pack(pady=10, padx=10)  # Empaqueta el control deslizante de altura con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

label_altura_valor = customtkinter.CTkLabel(master=frame_1, text="Altura: 0 m")  # Crea una etiqueta para mostrar el valor de la altura.
label_altura_valor.pack(pady=10, padx=10)  # Empaqueta la etiqueta de valor de altura con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

button_calcular = customtkinter.CTkButton(master=frame_1, text="Calcular IMC", command=lambda: calcular_imc(label_peso_valor.cget("text"), label_altura_valor.cget("text"), label_resultado))  # Crea un botón para calcular el IMC.
button_calcular.pack(pady=10, padx=10)  # Empaqueta el botón de cálculo de IMC con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

label_resultado = customtkinter.CTkLabel(master=frame_1, text="Resultado: ")  # Crea una etiqueta para mostrar el resultado del IMC.
label_resultado.pack(pady=10, padx=10)  # Empaqueta la etiqueta de resultado con espaciado vertical de 10 píxeles y espaciado horizontal de 10 píxeles.

def actualizar_label_peso(value, label):
    label.configure(text=f"Peso: {value:.2f} kg")

def actualizar_label_altura(value, label):
    label.configure(text=f"Altura: {value:.2f} m")

def calcular_imc(peso_str, altura_str, label_resultado):
    try:
        peso = float(peso_str.split()[1])  # Obtiene el valor numérico del peso desde el texto de la etiqueta.
        altura = float(altura_str.split()[1])  # Obtiene el valor numérico de la altura desde el texto de la etiqueta.

        # Verifica si los valores de peso y altura están en los rangos válidos
        if not (0 < peso <= 265) or not (0 < altura <= 2.72):
            mostrar_error("Error", "Ingresa valores válidos para peso y altura.")
            return None

        imc = peso / (altura ** 2)  # Calcula el IMC
        clasificacion = clasificar_imc(imc)  # Obtiene la clasificación del IMC

        label_resultado.configure(text=f"Resultado: IMC: {imc:.2f}, Clasificación: {clasificacion}")  # Actualiza la etiqueta de resultado.
    except ValueError:
        mostrar_error("Error", "Ingresa valores numéricos válidos para peso y altura.")
        return None

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def mostrar_error(titulo, mensaje):
    messagebox.showerror(titulo, mensaje)

app.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
