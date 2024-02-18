import tkinter as tk
from tkinter import ttk

def celsiusToFarenheit(temperature):
    return (temperature * 1.8) + 32


def farenheitToCelsius(temperature):
    return (temperature - 32) * (5/9)


def celsiusToKelvin(temperature):
    return temperature + 273.15


def kelvinToCelsius(temperature):
    return temperature - 273.15


def kelvinToFarenheit(temperature):
    return ((temperature - 273.15) * 1.8) + 32


def farenheitToKelvin(temperature):
    return ((temperature - 32) * (5/9)) + 273.15


def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        choice = temperature_choice.get()
        result_text.set("")

        if choice == 1:
            result_text.set(f"Temperature in Kelvin: {celsiusToKelvin(temperature)} K\n"
                            f"Temperature in Fahrenheit: {celsiusToFarenheit(temperature)} F")
        elif choice == 2:
            result_text.set(f"Temperature in Celsius: {farenheitToCelsius(temperature)} C\n"
                            f"Temperature in Kelvin: {farenheitToKelvin(temperature)} K")
        elif choice == 3:
            result_text.set(f"Temperature in Celsius: {kelvinToCelsius(temperature)} C\n"
                            f"Temperature in Fahrenheit: {kelvinToFarenheit(temperature)} F")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number.")



root = tk.Tk()
root.title("Temperature Converter")


label_temperature = ttk.Label(root, text="Enter temperature:")
label_temperature.grid(row=0, column=0, padx=5, pady=5)
entry_temperature = ttk.Entry(root)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)


temperature_choice = tk.IntVar()
temperature_choice.set(1)  # Default to Celsius
radio_celsius = ttk.Radiobutton(
    root, text="Celsius", variable=temperature_choice, value=1)
radio_celsius.grid(row=1, column=0, padx=5, pady=5)
radio_fahrenheit = ttk.Radiobutton(
    root, text="Fahrenheit", variable=temperature_choice, value=2)
radio_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
radio_kelvin = ttk.Radiobutton(
    root, text="Kelvin", variable=temperature_choice, value=3)
radio_kelvin.grid(row=1, column=2, padx=5, pady=5)


button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=3, pady=10)


result_text = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_text)
label_result.grid(row=3, column=0, columnspan=3, pady=5)


root.mainloop()
