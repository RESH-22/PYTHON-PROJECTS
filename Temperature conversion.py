def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15


print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))
temp = float(input("Enter temperature value: "))

if choice == 1:
    print("Result:", celsius_to_fahrenheit(temp))
elif choice == 2:
    print("Result:", fahrenheit_to_celsius(temp))
elif choice == 3:
    print("Result:", celsius_to_kelvin(temp))
elif choice == 4:
    print("Result:", kelvin_to_celsius(temp))
else:
    print("Invalid choice")
