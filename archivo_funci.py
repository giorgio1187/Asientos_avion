# Inicializamos el arreglo multidimensional para los asientos y los convierta en cadena con str
asientos = [str(i) for i in range(1, 43)]

# Inicializamos los precios
precio_normal = 78900
precio_vip = 240000

# Inicializamos la lista de pasajeros
pasajeros = []

# aca la funcion muestra los asiento ordenados entre normales y Vip
def mostrar_asientos():
    print("Asientos disponibles:")
    for i in range(5):
        for j in range(6):
            print(f"| {asientos[i*6 + j]:>3} |", end=" ")#ocupamos la funcion just (:>3)para el espaciado entre todos los asientos
        print()
        print()
    print("|_________________          __________________|")
    print("                     VIP                       ")
    print("|_________________          __________________|")
    print()
    print()
    for i in range(5, 7):
        for j in range(6):
            print(f"| {asientos[i*6 + j]:>3} |", end=" ")#
        print()
        print()

def comprar_asiento():
    global pasajeros #
    nombre_pasajero = input("Ingrese su nombre: ")
    rut_pasajero = input("Ingrese su rut, sin guion: ")
    telefono_pasajero = input("Ingrese su teléfono con 9 al comienzo: ")
    banco_pasajero = input("Ingrese su banco: ")
    asiento_seleccionado = int(input("Seleccione un asiento disponible entre el 1 y el 42: "))
    if asiento_seleccionado >= 31 and asiento_seleccionado <= 42:
        precio = precio_vip
    else:
        precio = precio_normal
    if banco_pasajero.lower() == "banco duoc":
        precio *= 0.85
    print(f"El precio del asiento es: ${precio:.2f}")
    respuesta = input("¿Acepta el precio? (s/n): ")
    if respuesta.lower() == "s":
        asientos[asiento_seleccionado - 1] = "X"
        pasajeros.append({
            "asiento": asiento_seleccionado,
            "nombre": nombre_pasajero,
            "rut": rut_pasajero,
            "telefono": telefono_pasajero,
            "banco": banco_pasajero
        })
        print("Asiento comprado con éxito!")
    else:
        print("Operación cancelada.")

def anular_pasaje():
    global pasajeros
    asiento_anular = int(input("Ingrese el asiento a anular: "))
    for pasajero in pasajeros:
        if pasajero["asiento"] == asiento_anular:
            asientos[asiento_anular - 1] = str(asiento_anular)
            pasajeros.remove(pasajero)
            print("Asiento anulado con éxito!")
            return
    print("Asiento no encontrado.")

def modificar_datos():
    global pasajeros
    asiento_modificar = int(input("Ingrese el asiento a modificar: "))
    rut_modificar = input("Ingrese el rut del pasajero: ")
    for pasajero in pasajeros:
        if pasajero["asiento"] == asiento_modificar and pasajero["rut"] == rut_modificar:
            print("Seleccione el dato a modificar:")
            print("1. Nombre")
            print("2. Teléfono")
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1:
                pasajero["nombre"] = input("Ingrese el nuevo nombre: ")
            elif opcion == 2:
                pasajero["telefono"] = input("Ingrese el nuevo teléfono: ")
            print("Datos modificados con éxito!")
            return
    print("Asiento o rut no encontrado.")
    
def main():
    while True:
        print("Menú:")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            mostrar_asientos()
        elif opcion == 2:
            comprar_asiento()
        elif opcion == 3:
            anular_pasaje()
        elif opcion == 4:
            modificar_datos()
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
    
