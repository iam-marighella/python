texto = str(input("Digite seu nome completo: "))
print(texto.upper())
print(texto.lower())
print(len(texto.strip().replace(' ', '')))
dividido = texto.split()
print(len(dividido[0]))
