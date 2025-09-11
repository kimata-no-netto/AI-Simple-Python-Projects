import tkinter as tk
from tkinter import filedialog
import pygame

# Inicializar pygame mixer
pygame.mixer.init()

# Funciones
def cargar():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.wav")])
    if archivo:
        pygame.mixer.music.load(archivo)
        etiqueta.config(text=f"Reproduciendo: {archivo.split('/')[-1]}")

def reproducir():
    pygame.mixer.music.play()

def pausar():
    pygame.mixer.music.pause()

def continuar():
    pygame.mixer.music.unpause()

def detener():
    pygame.mixer.music.stop()

# Crear ventana
ventana = tk.Tk()
ventana.title("Reproductor de Música")

etiqueta = tk.Label(ventana, text="Ningún archivo cargado", font=("Arial", 12))
etiqueta.pack(pady=10)

boton_cargar = tk.Button(ventana, text="Cargar", command=cargar, width=12)
boton_cargar.pack(pady=5)

boton_reproducir = tk.Button(ventana, text="Reproducir", command=reproducir, width=12)
boton_reproducir.pack(pady=5)

boton_pausar = tk.Button(ventana, text="Pausar", command=pausar, width=12)
boton_pausar.pack(pady=5)

boton_continuar = tk.Button(ventana, text="Continuar", command=continuar, width=12)
boton_continuar.pack(pady=5)

boton_detener = tk.Button(ventana, text="Detener", command=detener, width=12)
boton_detener.pack(pady=5)

ventana.mainloop()
