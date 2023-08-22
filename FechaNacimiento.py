from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    fecha_nacimiento_str = input("Por favor, ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
    
    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Usa dd/mm/aaaa.")
        return

    edad = calcular_edad(fecha_nacimiento)
    
    print(f"Tu edad es: {edad} años.")

if __name__ == "__main__":
    main()