# 6. Crie um programa que converta a temperatura de Celsius para Fahrenheit.
tempCelsius = (float(input("Digite a temperatura em graus Celsius: ")))
tempFahrenheit = (((tempCelsius * 9) / 5) + 32)
print("{:.2f}°C é igual a {:.2f}°F".format(tempCelsius, tempFahrenheit))