# Reducción de Número de Teléfono

telefono = str()

telefono = input("Introduce un número de teléfono siguiendo el formato: +codigopaís-xxxxxxxxx-extensión:")
division = telefono.split('-')

if len(division[1])==3:
    print("El número de telefono sin prefijo y extensión es:", division[2])
else:
    print("El número de telefono sin prefijo y extensión es:", division[1])