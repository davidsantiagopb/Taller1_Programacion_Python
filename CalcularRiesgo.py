# Definir una función que calcule el riesgo de enfermedades coronarias
def calcular_riesgo_enfermedad_coronaria(edad, imc):
    
    riesgo = 0.5 * edad + 0.7 * imc
    
    return riesgo

# Solicitar al usuario su edad e IMC
edad = float(input("Ingresa tu edad: "))
imc = float(input("Ingresa tu índice de masa corporal (IMC): "))

# Calcular el riesgo
riesgo = calcular_riesgo_enfermedad_coronaria(edad, imc)

# Imprimir el resultado
print(f"El riesgo estimado de enfermedades coronarias es: {riesgo}%")