from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Inicializar geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

def obtener_coordenadas(ciudad):
    try:
        location = geolocator.geocode(ciudad, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"No se pudo encontrar la ubicación de {ciudad}.")
            return None
    except Exception as e:
        print(f"Error al obtener las coordenadas de {ciudad}: {e}")
        return None

def calcular_distancia(origen, destino):
    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)
    
    if coord_origen and coord_destino:
        distancia_km = geodesic(coord_origen, coord_destino).km
        distancia_mi = geodesic(coord_origen, coord_destino).miles
        return distancia_km, distancia_mi
    else:
        return None, None

def main():
    while True:
        print("Ingrese 's' para salir en cualquier momento.")
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino: ")
        if destino.lower() == 's':
            break

        distancia_km, distancia_mi = calcular_distancia(origen, destino)
        
        if distancia_km and distancia_mi:
            print(f"\nDe {origen} a {destino}:")
            print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
            print(f"Narrativa del viaje: Desde {origen} hasta {destino} se recorren aproximadamente {distancia_km:.2f} km ({distancia_mi:.2f} millas).\n")
        else:
            print(f"No se pudo calcular la distancia entre {origen} y {destino}. Asegúrese de que ambas ciudades sean válidas.\n")

if __name__ == "__main__":
    main()


