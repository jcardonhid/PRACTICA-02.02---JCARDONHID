# Precio en Euros / Centimos

precio = input("Introduce el precio del producto seleccionado en el € (ejemplo 10.25 €)")
precio2 = precio.split('.')
print("El precio del producto es:", precio2[0], "€ y", precio2[1], "centimos")