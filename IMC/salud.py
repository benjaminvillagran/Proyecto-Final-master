import customtkinter
import tkinterDnD
from tkinter import messagebox

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x780")
app.title("CustomTkinter IMC Calculator")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_peso = customtkinter.CTkLabel(master=frame_1, text="Peso:")
label_peso.pack(pady=10, padx=10)

slider_peso = customtkinter.CTkSlider(master=frame_1, from_=0, to=265, command=lambda value: actualizar_label_peso(value, label_peso_valor))
slider_peso.pack(pady=10, padx=10)

label_peso_valor = customtkinter.CTkLabel(master=frame_1, text="Peso: 0 kg")
label_peso_valor.pack(pady=10, padx=10)

label_altura = customtkinter.CTkLabel(master=frame_1, text="Altura:")
label_altura.pack(pady=10, padx=10)

slider_altura = customtkinter.CTkSlider(master=frame_1, from_=0, to=2.5, command=lambda value: actualizar_label_altura(value, label_altura_valor))
slider_altura.pack(pady=10, padx=10)

label_altura_valor = customtkinter.CTkLabel(master=frame_1, text="Altura: 0 m")
label_altura_valor.pack(pady=10, padx=10)

button_calcular = customtkinter.CTkButton(master=frame_1, text="Calcular IMC", command=lambda: calcular_imc(label_peso_valor.cget("text"), label_altura_valor.cget("text"), label_resultado))
button_calcular.pack(pady=10, padx=10)

label_resultado = customtkinter.CTkLabel(master=frame_1, text="Resultado: ")
label_resultado.pack(pady=10, padx=10)

def actualizar_label_peso(value, label):
    label.configure(text=f"Peso: {value:.2f} kg")

def actualizar_label_altura(value, label):
    label.configure(text=f"Altura: {value:.2f} m")

def calcular_imc(peso_str, altura_str, label_resultado):
    try:
        peso = float(peso_str.split()[1])  
        altura = float(altura_str.split()[1])  

        if not (0 < peso <= 265) or not (0 < altura <= 2.72):
            mostrar_error("Error", "Ingresa valores válidos para peso y altura.")
            return None

        imc = peso / (altura ** 2)
        clasificacion = clasificar_imc(imc)

        label_resultado.configure(text=f"Resultado: IMC: {imc:.2f}, Clasificación: {clasificacion}")
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


app.mainloop()
