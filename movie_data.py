from imdb import IMDb
import tkinter as tk
from tkinter import messagebox

# Crear instancia de IMDb
ia = IMDb()

def buscar_pelicula():
    nombre = entry.get()
    if not nombre:
        messagebox.showwarning("Error", "Ingresa el nombre de la película")
        return

    resultados = ia.search_movie(nombre)
    if resultados:
        pelicula = resultados[0]  # Tomar el primer resultado
        ia.update(pelicula)
        info_text.set(
            f"Título: {pelicula.get('title')}\n"
            f"Año: {pelicula.get('year')}\n"
            f"Género: {', '.join(pelicula.get('genres', []))}\n"
            f"Director: {', '.join([d['name'] for d in pelicula.get('directors', [])])}\n"
            f"Actores: {', '.join([a['name'] for a in pelicula.get('cast', [])[:5]])}\n"
            f"Sinopsis: {pelicula.get('plot', ['No disponible'])[0]}"
        )
    else:
        messagebox.showinfo("No encontrada", "Película no encontrada.")

# Crear ventana principal
root = tk.Tk()
root.title("Buscador de Películas IMDbPY")

# Entrada de película
tk.Label(root, text="Nombre de la película:").pack()
entry = tk.Entry(root, width=40)
entry.pack()

# Botón de búsqueda
tk.Button(root, text="Buscar", command=buscar_pelicula).pack(pady=5)

# Texto de información
info_text = tk.StringVar()
tk.Label(root, textvariable=info_text, justify="left", wraplength=400).pack()

root.mainloop()
