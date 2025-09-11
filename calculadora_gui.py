import tkinter as tk

def click_boton(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Caja de texto
entrada = tk.Entry(ventana, width=20, font=("Arial", 18))
entrada.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        b = tk.Button(ventana, text=texto, width=5, height=2, command=calcular)
    else:
        b = tk.Button(ventana, text=texto, width=5, height=2, command=lambda t=texto: click_boton(t))
    b.grid(row=fila, column=columna)

# Botón limpiar
borrar = tk.Button(ventana, text="C", width=5, height=2, command=limpiar)
borrar.grid(row=4, column=3)

ventana.mainloop()
