# Pedir al usuario que ingrese cuatro números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
numero4 = int(input("Ingrese el cuarto número: "))

# Crear una lista con los números ingresados
numeros = [numero1, numero2, numero3, numero4]

# Ordenar la lista de menor a mayor
numeros_ordenados = sorted(numeros)

# Mostrar los números ordenados
print("Números ordenados de menor a mayor:")
for numero in numeros_ordenados:
    print(numero)