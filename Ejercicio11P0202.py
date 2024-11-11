# Completar Cadena

nombre = input("Por favor ingresa el nombre del producto:")
precio = float(input("Ahora ingresa el precio del producto:"))
unidades = int(input("Tambien ingresa el numero de unidades en existencia:"))
total = float(precio*unidades)
print("{nombre}: {precio:6.2f} euros x {unidades:3.0f} = {total:8.2f}".format(nombre=nombre, precio=precio, unidades=unidades, total=total))