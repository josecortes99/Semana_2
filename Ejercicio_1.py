vuelo = {}
id_reser = 0
tipos_viaje = {"nacional" : 230000, "internacional" : 4200000}
flag = True
    
def cost_equi_prin(peso_eqi):
    if peso_eqi > 50:
        return "❌ No admitido (debe cancelar o viajar sin equipaje)"
    elif peso_eqi == 50:
        return 110000
    elif peso_eqi == 30:
        return 70000
    elif peso_eqi == 20:
        return 50000
    else:
        return "❌ No admitido (debe cancelar o viajar sin equipaje)" 
        
def cost_equi_mano(peso_mano):
    if peso_mano > 13:
        return "Rechazado"
    return "Permitido"


def reserva():
    global id_reser
    id_reser += 1
    id_reserva = f"COMP{id_reser:04d}"

    nombre = input("Ingrese el nombre: ")
    
    while True:
        tipo_viaje = input("Ingrese su tipo de viaje (nacional/internacional): ").strip().lower()
        if tipo_viaje in ["nacional", "internacional"]:
            break
        print("Opción no válida. Intente nuevamente.")

    if tipo_viaje == "nacional":
        destino = "Bogotá → Medellín"
    else:
        destino = "Bogotá → España"
    
    while True:
        try:
            peso_eqi_prin = int(input("Ingrese el peso del equipaje en kg (mínimo 20 kg, opciones recomendadas: 20, 30, 50): "))
            if peso_eqi_prin in [20, 30, 50]:  
                break
            elif peso_eqi_prin >= 51:  
                print("❌ No admitido (debe cancelar o viajar sin equipaje)")
                break
        except ValueError:
            print("Error: Ingrese un número válido.")

    equi_prin = cost_equi_prin(peso_eqi_prin)
    
    while True:
        equi_mano = input("¿Lleva equipaje de mano? (si/no): ").lower()
        if equi_mano in ["si", "no"]:
            break
        print("Opción no válida. Intente nuevamente.")

    peso_mano = 0
    if equi_mano == "si":
        while True:
            try:
                peso_mano = int(input("Ingrese el peso del equipaje de mano en kg: "))
                break
            except ValueError:
                print("Error: Ingrese un número válido.")

    fecha = input("Ingrese la fecha del viaje (YYYY-MM-DD): ")
    
    precio_base = tipos_viaje[tipo_viaje]
    costo_total = precio_base + (equi_prin if equi_prin is not None else 0)

    reser = {
        "Id_reserva": id_reserva,
        "nombre": nombre,
        "destino" : destino,
        "fecha_viaje": fecha,
        "tipo_viaje": tipo_viaje,
        "Estado del equipaje principal": f"costo: {equi_prin}",
        "Estado del equipaje de mano": cost_equi_mano(peso_mano) if equi_mano == "si" else "No lleva",
        "Costo total del viaje": f"{costo_total} COP"

        
    }

    vuelo[id_reser] = reser
    print("\nReserva creada exitosamente:")
    print(vuelo)

def reporte_admin():
    print("\n--- Reporte para admins ---")
    print("1. Total ")
    print("2. Total recaudado por fecha")
    print("3. Total de pasajeros")
    print("4. Total de pasajeros por tipo de viaje")
    print("5. Buscar reserva por Id")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        total = sum(int(reserva["Costo total del viaje"].split()[0]) for reserva in vuelo.values())
        print(f" Total recaudado: ${total:,.0f}")
    
    elif opcion == "2":
        fecha_buscar = input("Ingresa la fecha (ej: 2025-05-09): ")
        total = sum(int(reserva["Costo total del viaje"].split()[0]) for reserva in vuelo.values() if reserva["fecha_viaje"] == fecha_buscar)
        print(f" Total recaudado para {fecha_buscar}: ${total:,.0f}")

    elif opcion == "3":
        print(f" Total de pasajeros procesados: {len(vuelo)}")

    elif opcion == "4":
        nacionales = sum(1 for reserva in vuelo.values() if reserva["tipo_viaje"] == "nacional")
        internacionales = sum(1 for reserva in vuelo.values() if reserva["tipo_viaje"] == "internacional")
        print(f" Nacionales: {nacionales}")
        print(f" Internacionales: {internacionales}")

    elif opcion == "5":
        id_buscar = input("Ingrese el ID de reserva (ej: COMP0001): ").strip().upper()
        if id_buscar in vuelo:
            reserva = vuelo[id_buscar]
            print("\n DETALLE DE LA RESERVA")
            print(f"ID: {reserva['Id_reserva']}")
            print(f"Nombre: {reserva['nombre']}")
            print(f"Destino: {reserva['destino']}")
            print(f"Fecha: {reserva['fecha_viaje']}")
            print(f"Equipaje principal: {reserva['Estado del equipaje principal']}")
            print(f"Equipaje de mano: {reserva['Estado del equipaje de mano']}")
            print(f"Total: ${reserva['Costo total del viaje']}")
        else:
            print("Reserva no encontrada.")

    else:
        print("Opción inválida.")
     
def menu():
    while True:
        print("\n----- Bienvenido a Airvac-----")
        print("1. gestionar reserva: ")
        print("2.Ver reporte administrativo")
        print("3.Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nIngrese solo numero enteros")

        if opcion == 1:
            reserva()
        elif opcion == 2:
            reporte_admin()
        elif opcion == 3:
            print("----- Hasta luego -----")
            break
        else:
            print("Opción no válida.")

menu()


