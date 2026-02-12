"""
Temperature Conversion Logic
Used for converting temperature values between
Celsius, Fahrenheit, and Kelvin.
"""

def celsius_to_others(c):
    fahrenheit = (c * 9 / 5) + 32
    kelvin = c + 273.15
    return fahrenheit, kelvin


def fahrenheit_to_others(f):
    celsius = (f - 32) * 5 / 9
    kelvin = celsius + 273.15
    return celsius, kelvin


def kelvin_to_others(k):
    celsius = k - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    return celsius, fahrenheit
