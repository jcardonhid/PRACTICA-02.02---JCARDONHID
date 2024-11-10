# Cálculo de las Letras de un Nombre.

nombre=""

nombre=input("Por favor introduce tu nombre:")
nombre_completo = nombre.replace(' ','')
medida=len(nombre_completo)
print("Tu nombre es:", nombre, "y contiene", medida, "letras.")