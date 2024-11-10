# Inversión de Frase

frase = input("Introduce una frase que te llame la atención:")
longitud = -len(frase)-1
frase_inversa = frase[-1:longitud:-1]
print(frase_inversa)