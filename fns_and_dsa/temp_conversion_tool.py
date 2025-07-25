FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_input = input("enter the temperature to convert: ")
measurement = input("enter C for celsius or F for fahrenheit: ").upper() 
if temperature_input.replace('.', '', 1).isdigit() or (temperature_input.startswith('-') and temperature_input[1:].replace('.', '', 1).isdigit()):
    temperature = float(temperature_input)
    
    if measurement == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif measurement == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
