class Temperature:

    def convertFahrenheit(self, celsius):
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def convertCelsius(self, fahrenheit):
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5/9
        return celsius


# Create object of class
temp = Temperature()

# Example usage
c = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", temp.convertFahrenheit(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", temp.convertCelsius(f))
