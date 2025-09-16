"""
Simple YouTube to MP3 converter with Tkinter GUI (using yt-dlp).

Features:
- Paste a YouTube URL
- Choose output folder
- Download audio and convert to MP3 (via ffmpeg)

Dependencies:
- yt-dlp
- tkinter (comes with Python)
- ffmpeg must be installed and available in PATH

Usage:
python youtube_to_mp3_tk.py

Legal: Only download content you own or that is explicitly allowed by the uploader's license.
"""

import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

# Function to handle the download and conversion
def download_convert(url, folder, status_label):
    try:
        status_label.config(text="Descargando y convirtiendo...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')
            status_label.config(text=f"¡Listo! Guardado en: {os.path.join(folder, title + '.mp3')}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error al descargar.")

# Function to start the download in a thread
def start_download(url_entry, folder_entry, status_label):
    url = url_entry.get().strip()
    folder = folder_entry.get().strip()
    if not url:
        messagebox.showwarning("Atención", "Por favor ingresa una URL.")
        return
    if not folder:
        messagebox.showwarning("Atención", "Por favor elige una carpeta.")
        return
    threading.Thread(target=download_convert, args=(url, folder, status_label), daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("YouTube a MP3 (yt-dlp)")
root.geometry("500x300")

# URL input
url_label = tk.Label(root, text="URL de YouTube:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Folder selection (debajo de la URL)
folder_label = tk.Label(root, text="Carpeta de destino:")
folder_label.pack(pady=5)
folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)
folder_entry = tk.Entry(folder_frame, width=45)
folder_entry.pack(side=tk.LEFT, padx=5)
folder_button = tk.Button(folder_frame, text="Elegir", command=lambda: folder_entry.delete(0, tk.END) or folder_entry.insert(0, filedialog.askdirectory()))
folder_button.pack(side=tk.LEFT, padx=5)

# Status label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

# Download and exit buttons (más abajo)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
download_button = tk.Button(button_frame, text="Descargar y Convertir", command=lambda: start_download(url_entry, folder_entry, status_label))
download_button.pack(side=tk.LEFT, padx=10)
exit_button = tk.Button(button_frame, text="Salir", command=root.quit)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
