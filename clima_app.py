import tkinter as tk
import requests

# 🔹 Diccionario de ciudades con coordenadas (ejemplo inicial)
CIUDADES = {
    "Lima": {"lat": -12.0464, "lon": -77.0428},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "Bogotá": {"lat": 4.7110, "lon": -74.0721}
}

URL = "https://api.open-meteo.com/v1/forecast"

def obtener_clima():
    ciudad = entrada.get()
    if ciudad not in CIUDADES:
        resultado.config(text="❌ Ciudad no registrada.\nPrueba Lima, Madrid, Buenos Aires...")
        return
    
    lat = CIUDADES[ciudad]["lat"]
    lon = CIUDADES[ciudad]["lon"]

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    try:
        r = requests.get(URL, params=params, timeout=5)
        datos = r.json()

        if "current_weather" not in datos:
            resultado.config(text="❌ No se pudo obtener el clima")
            return

        clima = datos["current_weather"]
        temp = clima["temperature"]
        viento = clima["windspeed"]

        texto = (
            f"🌍 Ciudad: {ciudad}\n"
            f"🌡️ Temperatura: {temp}°C\n"
            f"💨 Viento: {viento} km/h"
        )
        resultado.config(text=texto)

    except Exception as e:
        resultado.config(text=f"⚠️ Error: {e}")

# ------------------------------
# 🎨 Interfaz con Tkinter
# ------------------------------
ventana = tk.Tk()
ventana.title("App del Clima (Open-Meteo)")
ventana.geometry("300x250")

# Entrada de ciudad
entrada = tk.Entry(ventana, width=25, font=("Arial", 12))
entrada.pack(pady=10)
entrada.insert(0, "Lima")  # valor por defecto

# Botón
boton = tk.Button(ventana, text="Consultar clima", command=obtener_clima)
boton.pack(pady=5)

# Resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
resultado.pack(pady=10)

ventana.mainloop()
