import customtkinter
from email.mime.text import MIMEText
from smtplib import SMTP
from tkinter import messagebox
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class EmailSenderApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Enviar email")
        self.geometry("400x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sender_email_label = customtkinter.CTkLabel(self, text="Remitente:")
        self.sender_email_label.grid(row=0, column=0, pady=10)
        self.sender_email_entry = customtkinter.CTkEntry(self)
        self.sender_email_entry.grid(row=0, column=1, pady=10)

        self.receiver_email_label = customtkinter.CTkLabel(self, text="Destinatario:")
        self.receiver_email_label.grid(row=1, column=0, pady=10)
        self.receiver_email_entry = customtkinter.CTkEntry(self)
        self.receiver_email_entry.grid(row=1, column=1, pady=10)

        self.subject_label = customtkinter.CTkLabel(self, text="Razon:")
        self.subject_label.grid(row=2, column=0, pady=10)
        self.subject_entry = customtkinter.CTkEntry(self)
        self.subject_entry.grid(row=2, column=1, pady=10)

        self.message_label = customtkinter.CTkLabel(self, text="Mensaje:")
        self.message_label.grid(row=3, column=0, pady=10)

        self.message_text = customtkinter.CTkTextbox(self)
        self.message_text.grid(row=3, column=1, pady=10)

        self.send_button = customtkinter.CTkButton(self, text="Enviar email", command=self.send_email)
        self.send_button.grid(row=4, column=0, columnspan=2, pady=20)

    def send_email(self):
        sender_email = self.sender_email_entry.get()
        receiver_email = self.receiver_email_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end-1c")

        if sender_email and receiver_email and subject and message:
            try:
                # Configurar el servidor SMTP
                servidor = SMTP("smtp.gmail.com", 587)
                servidor.ehlo()
                servidor.starttls()

                # Configurar el mensaje
                mensaje_correo = MIMEText(message)
                mensaje_correo["From"] = sender_email
                mensaje_correo["To"] = receiver_email
                mensaje_correo["Subject"] = subject

                # Iniciar sesión
                servidor.login(sender_email, "xknosiomkxotftxz")

                # Enviar el correo electrónico
                servidor.sendmail(sender_email, receiver_email, mensaje_correo.as_string())
                # Terminar la conexión
                servidor.quit()
                messagebox.showinfo("Perfecto", "Email Enviado")

            except Exception as e:
                print("Error enviando el email:", str(e))
        else:
            print("Please fill in all fields before sending the email.")

if __name__ == "__main__":
    app = EmailSenderApp()
    app.mainloop()