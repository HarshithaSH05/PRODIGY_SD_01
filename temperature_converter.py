"""
Temperature Conversion Program
--------------------------------
Converts temperature values between Celsius, Fahrenheit,
and Kelvin scales.

Language: Python 3
"""

def celsius_to_others(c):
    f = (c * 9 / 5) + 32
    k = c + 273.15
    return f, k


def fahrenheit_to_others(f):
    c = (f - 32) * 5 / 9
    k = c + 273.15
    return c, k


def kelvin_to_others(k):
    c = k - 273.15
    f = (c * 9 / 5) + 32
    return c, f


def get_temperature():
    while True:
        try:
            return float(input("Enter temperature value: "))
        except ValueError:
            print("❌ Please enter a valid number.")


def get_unit():
    while True:
        unit = input("Enter unit (C / F / K): ").strip().upper()
        if unit in ["C", "F", "K"]:
            return unit
        print("❌ Invalid unit. Use C, F, or K.")


def main():
    print("\n=== Temperature Conversion Program ===\n")

    temp = get_temperature()
    unit = get_unit()

    print("\nConverted Values:")

    if unit == "C":
        f, k = celsius_to_others(temp)
        print(f"Fahrenheit: {f:.2f} °F")
        print(f"Kelvin: {k:.2f} K")

    elif unit == "F":
        c, k = fahrenheit_to_others(temp)
        print(f"Celsius: {c:.2f} °C")
        print(f"Kelvin: {k:.2f} K")

    elif unit == "K":
        c, f = kelvin_to_others(temp)
        print(f"Celsius: {c:.2f} °C")
        print(f"Fahrenheit: {f:.2f} °F")

    print("\n✅ Conversion Complete\n")


if __name__ == "__main__":
    main()
