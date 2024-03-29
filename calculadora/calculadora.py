import customtkinter as ctk  # Importa la biblioteca personalizada customtkinter con el alias 'ctk'.
from tkinter import messagebox  # Importa la clase 'messagebox' de tkinter.

# Mudando el tema a 'dark'
ctk.set_appearance_mode('dark')

# Configurando la ventana
ventana = ctk.CTk()  # Crea una ventana utilizando la clase personalizada CTk.
ventana.geometry('361x354+423+159')  # Configura las dimensiones y la posición de la ventana.

def calcular():
    try:
        output.configure(state="normal")  # Habilita la edición del campo de texto de salida.
        calculo = output.get('0.0', 'end')  # Obtiene la expresión matemática ingresada.
        resultado = eval(calculo)  # Evalúa la expresión matemática.
        output.delete('0.0', 'end')  # Limpia el campo de texto de salida.
        output.insert('0.0', resultado)  # Muestra el resultado en el campo de texto de salida.
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")
        output.delete('0.0', 'end')  # Limpia el campo de texto de salida en caso de error.
    except SyntaxError:
        messagebox.showerror("Error", "Expresión matemática incorrecta.")
        output.delete('0.0', 'end')  # Limpia el campo de texto de salida en caso de error.
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        output.delete('0.0', 'end')  # Limpia el campo de texto de salida en caso de error.
    finally:
        output.configure(state="disabled")  # Deshabilita la edición del campo de texto de salida.

def btnFunction(caracter):
    output.configure(state="normal")  # Habilita la edición del campo de texto de salida.
    output.insert('end', caracter)  # Inserta el carácter en la posición actual del campo de texto de salida.
    output.configure(state="disabled")  # Deshabilita la edición del campo de texto de salida.

def btnDelete():
    output.configure(state="normal")  # Habilita la edición del campo de texto de salida.
    output.delete('0.0', 'end')  # Limpia el campo de texto de salida.
    output.configure(state="disabled")  # Deshabilita la edición del campo de texto de salida.

# Campo donde el usuario ingresará los números y la operación
output = ctk.CTkTextbox(ventana, width=340, height=50, corner_radius=10, border_width=5, border_color='#042940', font=(('Arial', 50)))
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
output.configure(state="disabled")  # Inicialmente, deshabilita la edición del campo de texto de salida.

# Botones
btn1 = ctk.CTkButton(ventana, text='1', command=lambda: btnFunction(1), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn1.grid(row=1, column=0, padx=5, pady=5)

# Los otros botones siguen aquí...
btn2 = ctk.CTkButton(ventana, text='2', command=lambda: btnFunction(2), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = ctk.CTkButton(ventana, text='3', command=lambda: btnFunction(3), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn3.grid(row=1, column=2, padx=5, pady=5)

btn4 = ctk.CTkButton(ventana, text='4', command=lambda: btnFunction(4), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = ctk.CTkButton(ventana, text='5', command=lambda: btnFunction(5), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = ctk.CTkButton(ventana, text='6', command=lambda: btnFunction(6), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn6.grid(row=2, column=2, padx=5, pady=5)

btn7 = ctk.CTkButton(ventana, text='7', command=lambda: btnFunction(7), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn7.grid(row=3, column=0, padx=5, pady=5)

btn8 = ctk.CTkButton(ventana, text='8', command=lambda: btnFunction(8), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn8.grid(row=3, column=1, padx=5, pady=5)

btn9 = ctk.CTkButton(ventana, text='9', command=lambda: btnFunction(9), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn9.grid(row=3, column=2, padx=5, pady=5)

btn0 = ctk.CTkButton(ventana, text='0', command=lambda: btnFunction(0), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn0.grid(row=4, column=0, padx=5, pady=5)

btn_limpiar = ctk.CTkButton(ventana, text='C', command=btnDelete, corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_limpiar.grid(row=4, column=1, padx=5, pady=5)

btn_calcular = ctk.CTkButton(ventana, text='=', command=calcular, corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_calcular.grid(row=4, column=2, padx=5, pady=5)

btn_sumar = ctk.CTkButton(ventana, text='+', command=lambda: btnFunction('+'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_sumar.grid(row=1, column=3, padx=5, pady=5)

btn_restar = ctk.CTkButton(ventana, text='-', command=lambda: btnFunction('-'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_restar.grid(row=2, column=3, padx=5, pady=5)

btn_multiplicar = ctk.CTkButton(ventana, text='x', command=lambda: btnFunction('*'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_multiplicar.grid(row=3, column=3, padx=5, pady=5)

btn_dividir = ctk.CTkButton(ventana, text='/', command=lambda: btnFunction('/'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_dividir.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
