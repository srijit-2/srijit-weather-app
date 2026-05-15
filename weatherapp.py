import tkinter as tk
from tkinter import messagebox
import requests



API_KEY = "b0742acbe1e142ee864130903261405"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "yes"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", "City not found")
            return

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        feels_like = data["current"]["feelslike_c"]

        weather_result.config(
            text=
            f"📍 City: {city_name}, {country}\n\n"
            f"🌡 Temperature: {temperature}°C\n"
            f"☁ Condition: {condition}\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind_speed} km/h\n"
            f"🤗 Feels Like: {feels_like}°C"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))




root = tk.Tk()
root.title("srijit's Weather App")
root.geometry("500x550")
root.config(bg="#4facfe")


heading = tk.Label(
    root,
    text="SRIJIT'S WEATHER APP",
    font=("Arial", 24, "bold"),
    bg="#4facfe",
    fg="white"
)

heading.pack(pady=20)



city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    bd=3
)

city_entry.pack(pady=10)



search_button = tk.Button(
    root,
    text="Search Weather",
    font=("Arial", 14, "bold"),
    bg="#007bff",
    fg="white",
    padx=10,
    pady=5,
    command=get_weather
)

search_button.pack(pady=15)

weather_result = tk.Label(
    root,
    text="Enter a city name above",
    font=("Arial", 14),
    bg="white",
    fg="#333",
    width=38,
    height=12,
    justify="left",
    anchor="nw",
    padx=15,
    pady=15
)

weather_result.pack(pady=20)
root.mainloop()