class Temperature:
    def __init__(self, value):
        self.value = value

    def convertFahrenheit(self):
        fahrenheit = (self.value * 9/5) + 32
        return fahrenheit

    def convertCelsius(self):
        celsius = (self.value - 32) * 5/9
        return celsius


temp1 = Temperature(25)  
print("25°C in Fahrenheit:", temp1.convertFahrenheit())

temp2 = Temperature(77)   
print("77°F in Celsius:", temp2.convertCelsius())
