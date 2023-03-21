# escreva um programa que converta uma temperatura digitada em °C para °F e °K.
celcius = float(input('Digite a temperatura atual em °C : '))
fahrenheit = (celcius * 1.8 + 32)
kelvin = (celcius + 273)
print('A temperatura de {}°C corresponde a \n {}°F ! ou \n {}°K ! '.format(
    celcius, fahrenheit, kelvin))
