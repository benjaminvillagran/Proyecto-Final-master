import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import customtkinter
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class MusicPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reproductor de Música")
        self.geometry("500x400")

        mixer.init()

        self.playlist = []
        self.current_song_index = 0
        self.song_length = 0

        self.create_widgets()

    def create_widgets(self):
        self.btn_add_song = customtkinter.CTkButton(self, text="Agregar Canciones", command=self.add_songs)
        self.btn_add_song.pack(pady=(10, 10))

        self.btn_play = customtkinter.CTkButton(self, text="Reproducir", command=self.play_song)
        self.btn_play.pack(pady=10)

        self.btn_stop = customtkinter.CTkButton(self, text="Detener", command=self.stop_song)
        self.btn_stop.pack(pady=10)

        self.btn_next = customtkinter.CTkButton(self, text="Siguiente", command=self.next_song)
        self.btn_next.pack(pady=10)

        self.lbl_current_song = customtkinter.CTkLabel(self, text="", font=('Helvetica', 14))
        self.lbl_current_song.pack(pady=10)

        self.volume_scale = tk.Scale(self, from_=0, to=100, orient="horizontal", command=self.set_volume)
        self.volume_scale.set(50)
        self.volume_scale.pack(pady=10)

        self.progress_bar = customtkinter.CTkProgressBar(self, orientation="horizontal", mode="determinate")
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0.0)
    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Selecciona Canciones", filetypes=[("Archivos MP3", "*.mp3")])
        self.playlist.extend(songs)

    def load_song(self):
        file_path = self.playlist[self.current_song_index]
        mixer.music.load(file_path)
        self.song_length = mixer.Sound(file_path).get_length()
        self.progress_bar.set(0.0)  
        self.progress_bar.start()   
    def stop_song(self):
        mixer.music.stop()
        self.lbl_current_song.configure(text="")
        self.progress_bar.stop()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play_song()

    def set_volume(self, volume):
        mixer.music.set_volume(float(volume) / 100)

    def play_song(self):
        file_path = self.playlist[self.current_song_index]
        self.load_song()

        mixer.music.play()
        self.lbl_current_song.configure(text=f"Reproduciendo: {os.path.basename(file_path)}")
        self.update_progress()

    def update_progress(self):
        current_time = mixer.music.get_pos() / 1000

        if self.song_length > 0:
            progress_percentage = current_time / self.song_length
            self.progress_bar.set(progress_percentage)

        if current_time < self.song_length:

            self.after(100, self.update_progress)
        else:
            self.progress_bar.set(1.0)  
            self.progress_bar.stop()  
if __name__ == "__main__":
    app = MusicPlayerApp()
    app.mainloop()
