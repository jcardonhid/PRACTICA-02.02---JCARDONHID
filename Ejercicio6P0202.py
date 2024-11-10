# Modificación de Vocales en Frase

frase = input("Introduce una frase que te guste:")
vocal = input("Introduce la vocal que deceas cambiar a mayuscula en tu frase:")

vocal_ma = vocal.upper()
vocal_mi = vocal.lower()

frase = frase.replace(vocal_mi,vocal_ma)

print(frase)