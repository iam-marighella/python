var = input("Digite algo: ")
print("O tipo primitivo de {} é {}".format(var, type(var)))
print("O que você digitou...")
print("Só tem letras? {}".format(var.isalpha()))
print("Tem letras e/ou números? {}".format(var.isalnum()))
print("Só tem números? {}".format(var.isnumeric()))
print("Só tem espaços? {}".format(var.isspace()))
print("É decimal? {}".format(var.isdecimal()))
print("Só tem letras maíusculas? {}".format(var.isupper()))
print("Só tem letras minúsculas? {}".format(var.islower()))