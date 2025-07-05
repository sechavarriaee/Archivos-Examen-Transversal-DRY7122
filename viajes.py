from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import time
import sys

def obtener_coordenadas(ciudad):
    """Obtiene las coordenadas (latitud, longitud) de una ciudad"""
    geolocator = Nominatim(user_agent="medidor_distancias")
    location = geolocator.geocode(ciudad)
    if not location:
        raise ValueError("Ciudad no encontrada")
    return (location.latitude, location.longitude)

def seleccionar_medio_transporte():
    """Permite al usuario seleccionar el medio de transporte"""
    medios = {
        '1': 'auto',
        '2': 'bus',
        '3': 'avión',
        '4': 'bicicleta'
    }
    
    print("\nMedios de transporte disponibles:")
    print("1. Auto")
    print("2. Bus")
    print("3. Avión")
    print("4. Bicicleta")
    
    while True:
        opcion = input("Seleccione el medio de transporte (1-4): ")
        if opcion in medios:
            return medios[opcion]
        print("Opción inválida. Intente nuevamente.")

def calcular_tiempo_viaje(distancia_km, medio):
    """Calcula el tiempo aproximado de viaje según el medio de transporte"""
    velocidades = {
        'auto': 90,      # km/h
        'bus': 70,       # km/h
        'avión': 800,    # km/h
        'bicicleta': 15   # km/h
    }
    
    velocidad = velocidades.get(medio, 50)
    horas = distancia_km / velocidad
    
    # Ajuste para vuelos cortos (tiempo de check-in, etc.)
    if medio == 'avión' and horas < 2:
        horas += 1.5
    
    horas_enteras = int(horas)
    minutos = int((horas % 1) * 60)
    
    return f"{horas_enteras} horas y {minutos} minutos"

def mostrar_resultados(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, medio, tiempo_viaje):
    """Muestra los resultados del cálculo de distancia y tiempo"""
    print("\n" + "="*50)
    print("RESULTADOS DEL VIAJE".center(50))
    print("="*50)
    print(f"\nDe: {ciudad_origen}, Chile")
    print(f"A:  {ciudad_destino}, Argentina")
    print("\n" + "-"*50)
    print(f"Distancia en kilómetros: {distancia_km:.2f} km")
    print(f"Distancia en millas: {distancia_millas:.2f} mi")
    print(f"Duración estimada ({medio}): {tiempo_viaje}")
    print("\n" + "-"*50)
    
    # Narrativa del viaje
    print("\nNARRATIVA DEL VIAJE:")
    print(f"Tu viaje desde {ciudad_origen}, Chile hasta {ciudad_destino}, Argentina")
    print(f"cubrirá una distancia de aproximadamente {distancia_km:.0f} kilómetros")
    print(f"({distancia_millas:.0f} millas). Viajando en {medio}, el trayecto")
    print(f"tomará alrededor de {tiempo_viaje}.")
    
    # Mensaje especial según medio de transporte
    if medio == 'avión':
        print("\nRecomendación: Llegue al aeropuerto con al menos 2 horas de anticipación.")
    elif medio == 'bicicleta':
        print("\nRecomendación: Lleve suficiente agua y protección solar para el viaje.")
    else:
        print("\nRecomendación: Revise las condiciones del tránsito antes de salir.")
    
    print("\n¡Buen viaje!\n")

def main():
    """Función principal del programa"""
    while True:
        print("\n" + "="*50)
        print("MEDIDOR DE DISTANCIAS CHILE-ARGENTINA".center(50))
        print("="*50)
        print("\nIngrese las ciudades para medir la distancia")
        print("Presione 's' para salir en cualquier momento\n")
        
        # Verificar si el usuario quiere salir
        ciudad_origen = input("Ciudad de origen (Chile): ").strip()
        if ciudad_origen.lower() == 's':
            print("\nGracias por usar el medidor de distancias. ¡Hasta pronto!")
            sys.exit()
            
        ciudad_destino = input("Ciudad de destino (Argentina): ").strip()
        if ciudad_destino.lower() == 's':
            print("\nGracias por usar el medidor de distancias. ¡Hasta pronto!")
            sys.exit()
        
        try:
            # Obtener coordenadas
            loc_origen = obtener_coordenadas(ciudad_origen + ", Chile")
            loc_destino = obtener_coordenadas(ciudad_destino + ", Argentina")
            
            # Seleccionar medio de transporte
            medio_transporte = seleccionar_medio_transporte()
            
            # Calcular distancias
            distancia_km = geodesic(loc_origen, loc_destino).kilometers
            distancia_millas = distancia_km * 0.621371
            
            # Calcular tiempo de viaje
            tiempo_viaje = calcular_tiempo_viaje(distancia_km, medio_transporte)
            
            # Mostrar resultados
            mostrar_resultados(
                ciudad_origen, 
                ciudad_destino, 
                distancia_km, 
                distancia_millas, 
                medio_transporte, 
                tiempo_viaje
            )
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Por favor verifique los nombres de las ciudades e intente nuevamente.")
            continue
        
        # Preguntar si desea realizar otra consulta
        otra_consulta = input("\n¿Desea medir otra distancia? (s/n): ").lower()
        if otra_consulta != 's':
            print("\nGracias por usar el medidor de distancias. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        sys.exit()
