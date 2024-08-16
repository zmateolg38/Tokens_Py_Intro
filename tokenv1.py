# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from nltk.tokenize import word_tokenize
import nltk

# Descargamos el recurso necesario de nltk si no está ya descargado
nltk.download('punkt')

# Solicita al usuario que ingrese el texto
text = input("Digita el texto #1 tokenizar: ")
text2 = input("Digita el texto #2 tokenizar: ")

# Imprime la longitud del texto
print("Longitud del texto #1:", len(text))
print("Longitud del texto: #2", len(text2))

# Tokeniza el texto en palabras
tokens = word_tokenize(text)
tokens2 = word_tokenize(text2)

# Imprime la lista de tokens
print("Tokens:", tokens)
print("Tokens:", tokens2)

# Imprime el primer token junto con los primeros 30 caracteres del texto en mayúsculas
if tokens:  # Verifica si hay tokens en la lista
    primer_token = tokens[0]
    primeros_30_caracteres_upper = text[:30].upper()
    primeros_30_caracteres_lower = text[:30].lower()
    primera_letra_mayuscula_capitalize=text[0:30].capitalize()  
    
    if tokens:
        segundo_token = tokens[0]
        primeros_30_caracteres_upperV2 = text2[:30].upper()
        primeros_30_caracteres_lowerV2 = text2[:30].lower()
        primera_letra_mayuscula_capitalizeV2=text2[0:30].capitalize()
    
    
    print("Texto en minuscula", primeros_30_caracteres_lower)
    print("Texto en Mayuscula", primeros_30_caracteres_upper)
    print("Texto en Mayuscula", primeros_30_caracteres_upperV2)
    print("Texto en Minuscula", primeros_30_caracteres_lowerV2)
    print("Texto en PLM: ", primera_letra_mayuscula_capitalizeV2)

    
    
    
    print("", "".join(map(str, [primer_token,", ",segundo_token])))
else:
    print("No se encontraron tokens.")