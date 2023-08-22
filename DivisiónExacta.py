# Solicita al usuario ingresar el dividendo y el divisor
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

# Verifica si el divisor es cero (lo cual no está permitido en la división)
if divisor != 0:
    cociente = dividendo // divisor  # Calcula el cociente
    residuo = dividendo % divisor    # Calcula el residuo

    if residuo == 0:
        print("La división es exacta.")
        print("Cociente:", cociente)
    else:
        print("La división no es exacta.")
        print("Cociente:", cociente)
        print("Residuo:", residuo)
else:
    print("Error: No se puede dividir por cero.")