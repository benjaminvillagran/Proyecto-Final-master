import tkinter as tk  # Importa la biblioteca tkinter con el alias 'tk'.
from tkinter import ttk, messagebox, filedialog  # Importa clases específicas de tkinter.
from tkinterdnd2 import TkinterDnD, DND_FILES  # Importa clases para manejar arrastrar y soltar.
from plyer import notification  # Importa la biblioteca plyer para notificaciones.
from tkcalendar import Calendar  # Importa la clase Calendar de la biblioteca tkcalendar.
from ttkthemes import ThemedTk  # Importa la clase ThemedTk de la biblioteca ttkthemes.

class CalendarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario App")
        self.master.geometry("500x500")

        # Cambiar el tema a modo oscuro
        self.master.set_theme("equilux")
        self.master.tk_setPalette(background='#26242f', foreground='white', activeBackground='#26242f', activeForeground='white')

        style = ttk.Style()
        style.configure("TEntry", fieldbackground='#26242f', foreground='white')
        style.map("TEntry", fieldbackground=[('readonly', '#26242f')])
        
        # 2. Agregar Eventos
        self.label_evento = tk.Label(self.master, text="Agregar Evento:", background="#26242f", foreground="white")
        self.label_evento.pack(pady=5)
        self.entry_evento = tk.Entry(self.master, width=30, background="#26242f", foreground="white")
        self.entry_evento.pack(pady=5)
        
        # Calendario
        self.label_calendario = tk.Label(self.master, text="Selecciona una fecha:", background="#26242f", foreground="white")
        self.label_calendario.pack(pady=5)
        self.calendario = Calendar(self.master, selectmode="day", date_pattern="yyyy-mm-dd", background="#26242f", foreground="white", headersbackground="#26242f")
        self.calendario.pack(pady=5)

        self.boton_agregar = tk.Button(self.master, text="Agregar Evento", command=self.agregar_evento, background="#26242f", foreground="white")
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = tk.Button(self.master, text="Eliminar Evento", command=self.eliminar_evento, background="#26242f", foreground="white")
        self.boton_eliminar.pack(pady=5)
        
        self.boton_exportar = tk.Button(self.master, text="Exportar Eventos", command=self.exportar_eventos)
        self.boton_exportar.pack(pady=5)
        
        self.boton_importar = tk.Button(self.master, text="Importar Eventos", command=self.importar_eventos)
        self.boton_importar.pack(pady=5)
        
        self.lista_eventos = tk.Listbox(self.master, height=5, selectbackground='yellow')
        self.lista_eventos.pack(pady=10)
        
        self.boton_modo_agenda = tk.Button(self.master, text="Modo Agenda", command=self.mostrar_agenda)
        self.boton_modo_agenda.pack(pady=5)

    def agregar_evento(self):
        evento = self.entry_evento.get()
        fecha = self.calendario.get_date()
        if evento and fecha:
            evento_completo = f"{fecha}: {evento}"
            self.lista_eventos.insert(tk.END, evento_completo)
            self.entry_evento.delete(0, tk.END)

    def eliminar_evento(self):
        seleccion = self.lista_eventos.curselection()
        if seleccion:
            self.lista_eventos.delete(seleccion)
        else:
            messagebox.showinfo("Eliminar Evento", "Selecciona un evento para eliminar.")

    def mostrar_agenda(self):
        eventos = self.lista_eventos.get(0, tk.END)
        if eventos:
            mensaje = "\n".join(eventos)
            notification.notify(
                title="Agenda del Día",
                message=mensaje,
                timeout=10
            )
        else:
            messagebox.showinfo("Agenda del Día", "No hay eventos para mostrar.")

    def mostrar_notificacion(self, mensaje):
        # Configuración de la notificación
        title = "Recordatorio"
        message = mensaje
        timeout = 10  # segundos

        # Mostrar notificación
        notification.notify(
            title=title,
            message=message,
            timeout=timeout
        )

    def importar_eventos(self):
        try:
            # Abre un cuadro de diálogo para seleccionar un archivo
            archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

            if archivo:
                with open(archivo, "r") as file:
                    eventos = file.readlines()

                # Agregar eventos a la lista
                self.lista_eventos.delete(0, tk.END)
                for evento in eventos:
                    self.lista_eventos.insert(tk.END, evento.strip())

                messagebox.showinfo("Importar Eventos", "Eventos importados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al importar eventos:\n{str(e)}")

    def exportar_eventos(self):
        try:
            # Abre un cuadro de diálogo para seleccionar la ubicación de guardado
            archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

            if archivo:
                # Obtiene los eventos de la lista
                eventos = self.lista_eventos.get(0, tk.END)

                # Guarda los eventos en el archivo
                with open(archivo, "w") as file:
                    file.write("\n".join(eventos))

                messagebox.showinfo("Exportar Eventos", "Eventos exportados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar eventos:\n{str(e)}")

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")  # Crea una instancia de ThemedTk con el tema "equilux".
    app = CalendarioApp(root)  # Crea una instancia de la aplicación CalendarioApp.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
