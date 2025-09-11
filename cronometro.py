import tkinter as tk

running = False
counter = 0

def iniciar():
    global running
    if not running:
        running = True
        contar()

def pausar():
    global running
    running = False

def reiniciar():
    global counter
    counter = 0
    label.config(text="00:00:00")

def contar():
    global counter
    if running:
        minutos, segundos = divmod(counter, 60)
        horas, minutos = divmod(minutos, 60)
        tiempo = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        label.config(text=tiempo)
        counter += 1
        ventana.after(1000, contar)  # llama de nuevo cada 1 segundo

# Crear ventana
ventana = tk.Tk()
ventana.title("Cronómetro")

label = tk.Label(ventana, text="00:00:00", font=("Arial", 40))
label.pack()

boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar, width=10)
boton_iniciar.pack(side=tk.LEFT, padx=5, pady=10)

boton_pausar = tk.Button(ventana, text="Pausar", command=pausar, width=10)
boton_pausar.pack(side=tk.LEFT, padx=5, pady=10)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar, width=10)
boton_reiniciar.pack(side=tk.LEFT, padx=5, pady=10)

ventana.mainloop()
