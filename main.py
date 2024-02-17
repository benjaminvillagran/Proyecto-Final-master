import tkinter as tk
import subprocess
import customtkinter
from PIL import Image
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Final")
        self.geometry("1100x580")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Crear un CTkImage para la imagen de fondo en tema oscuro
        dark_image_path = "C:\\Users\\villa\\Downloads\\Proyecto-Final-master\\hola_dark.jpg"
        dark_image = Image.open(dark_image_path)

        light_image_path = "C:\\Users\\villa\\Downloads\\Proyecto-Final-master\\hola_light.jpg"

        light_image = Image.open(light_image_path)

        # Crear un widget CTkLabel para mostrar la imagen de fondo
        bg_image = customtkinter.CTkImage(light_image=light_image, dark_image=dark_image, size=(1100, 580))
        image_label = customtkinter.CTkLabel(self, image=bg_image, text="")
        image_label.grid(row=0, column=0, rowspan=4, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrir_modulo_entretenimiento, text="Entretenimiento")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrir_modulo_utilidades, text="Utilidades")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=4, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_forget()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def abrir_ahorcado(self):
        try:
            subprocess.run(["python", "ahorcado/ahorcado.py"])
        except Exception as e:
            print("Error al abrir el juego:", e)

    def abrir_piedrapapeltijera(self):
        try:
            subprocess.run(["python", "PIEDRA PAPEL TIJERA/jueguito.py"])
        except Exception as e:
            print("Error al abrir el juego:", e)
    
    def abrir_tv(self):
        try:
            subprocess.run(["python","TV/futbol.py"])
        except Exception as e:
            print("Error ")

    def abrir_calculadora(self):
        try:
            subprocess.run(["python","calculadora/calculadora.py"])
        except Exception as e:
            print("Error")
    def abrir_imc(self):
        try:
            subprocess.run(["python","IMC/salud.py"])
        except Exception as e:
            print("Error")
    def abrir_bloc(self):
        try:
            subprocess.run(["python","BLOC DE NOTAS/bloc.py"])
        except Exception as e:
            print("Error")
    def abrir_gencontra(self):
        try:
            subprocess.run(["python","GENERADOR DE CONTRASEÑA/contraseñas.py"])
        except Exception as e:
            print("Error")
    def abrir_impuesto(self):
        try:
            subprocess.run(["python","IMPUESTO/impuesto.py"])
        except Exception as e:
            print("Error")
    def enviar_email(self):
        try:
            subprocess.run(["python","EMAIL/enviador_de_emails.py"])
        except Exception as e:
            print("Error")
    def abrir_modulo_entretenimiento(self):
        self.button_juego = customtkinter.CTkButton(self.main_frame, text="Juego", command=self.abrir_ahorcado)
        self.button_juego.grid(row=0, column=0, pady=20)

        self.button_tv = customtkinter.CTkButton(self.main_frame, text="TV", command=self.abrir_tv)
        self.button_tv.grid(row=1, column=0, pady=20)
        
        self.button_ahorcado = customtkinter.CTkButton(self.main_frame, text="Ahorcado", command=self.abrir_ahorcado)
        self.button_ahorcado.grid(row=2, column=0, pady=20)

        self.button_piedra_papel_tijera = customtkinter.CTkButton(self.main_frame, text="Piedra papel y Tijera", command=self.abrir_piedrapapeltijera)
        self.button_piedra_papel_tijera.grid(row=3, column=0, pady=20)     

        self.button_volver = customtkinter.CTkButton(self.main_frame, text="Volver", command=self.volver_al_menu_principal)
        self.button_volver.grid(row=4, column=0, pady=20)
        self.main_frame.grid(row=0, column=1, rowspan=4, columnspan=3, padx=20, pady=20, sticky="nsew")

    def abrir_modulo_utilidades(self):
        self.button_calculadora = customtkinter.CTkButton(self.main_frame, text="Calculadora", command=self.abrir_calculadora)
        self.button_calculadora.grid(row=0, column=0, pady=20)

        self.button_imc = customtkinter.CTkButton(self.main_frame, text="Calculadora IMC", command=self.abrir_imc)
        self.button_imc.grid(row=1, column=0, pady=20)

        self.button_contraseña = customtkinter.CTkButton(self.main_frame, text="Generador de contraseña", command=self.abrir_gencontra)
        self.button_contraseña.grid(row=2, column=0, pady=20)

        self.button_bloc = customtkinter.CTkButton(self.main_frame, text="Bloc de notas", command=self.abrir_bloc)
        self.button_bloc.grid(row=3, column=0, pady=20)
        
        self.button_impuesto = customtkinter.CTkButton(self.main_frame, text="Calculadora de impuestos", command=self.abrir_impuesto)
        self.button_impuesto.grid(row=0, column=1, pady=20)
    
        self.button_email    = customtkinter.CTkButton(self.main_frame, text="Enviar Email", command=self.enviar_email)
        self.button_email.grid(row=1,column=1,pady=20)

        self.button_volver = customtkinter.CTkButton(self.main_frame, text="Volver", command=self.volver_al_menu_principal)
        self.button_volver.grid(row=4, column=0, pady=20)
        self.main_frame.grid(row=0, column=1, rowspan=4, columnspan=3, padx=20, pady=20, sticky="nsew")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def limpiar_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    def volver_al_menu_principal(self):
        self.limpiar_frame()
        self.main_frame.grid_forget()
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()
