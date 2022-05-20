frase = input('Frase: ')

print('Total de letras: ',len(frase))
print('Total de palavras: ',len(frase.split(len(frase))))

texto = 'Uva, Pera e Banana'
print(texto.capitalize())
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.swapcase())
print(texto.startswith('Uva'))
print(texto.endswith('Uva'))
print(texto.split(' '))
print(texto.replace('Pera', 
'Maçã'))