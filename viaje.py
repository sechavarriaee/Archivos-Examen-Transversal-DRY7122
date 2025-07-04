import requests

def mostrar_menu():
    print("\n=== CALCULADOR DE RUTAS CHILE-ARGENTINA ===")
    print("1. Calcular nueva ruta")
    print("s. Salir")

def obtener_ruta():
    medios_transporte = {
        '1': 'car',
        '2': 'bike',
        '3': 'foot'
    }
    
    print("\nMedios de transporte disponibles:")
    print("1. Automóvil")
    print("2. Bicicleta")
    print("3. A pie")
    
    opcion = input("Seleccione medio de transporte (1-3): ").strip()
    vehiculo = medios_transporte.get(opcion, 'car')
    
    origen = input("Ciudad de Origen (Chile): ").strip() + ", Chile"
    destino = input("Ciudad de Destino (Argentina): ").strip() + ", Argentina"
    
    API_KEY = "9972f6e3-c1cb-47a1-91ac-35985de556fc"
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle={vehiculo}&locale=es&key={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Error desconocido')}")
            return
        
        if not data.get('paths'):
            print("No se encontró ruta entre las ciudades especificadas")
            return
            
        ruta = data['paths'][0]
        distancia_km = ruta['distance'] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_horas = ruta['time'] / 3600000
        
        print(f"\nDistancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"Duración: {duracion_horas:.2f} horas")
        
        if ruta.get('instructions'):
            print("\nNarrativa del viaje:")
            for i, paso in enumerate(ruta['instructions'], 1):
                print(f"{i}. {paso['text']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ").strip().lower()
        
        if opcion == 's':
            print("Saliendo del programa...")
            break
        elif opcion == '1':
            obtener_ruta()
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
