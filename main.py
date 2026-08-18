from datetime import datetime, timedelta

from modelos import (
    Asiento,
    Destino,
    Pago,
    Pasajero,
    Reserva,
    TarjetaEmbarque,
    Usuario,
    Vuelo,
)


#destinos + vuelos


destino_cordoba = Destino(
    pais="Argentina",
    ciudad="Cordoba",
    descripcion="Aeropuerto Internacional Ambrosio Taravella",
)


destino_bariloche = Destino(
    pais="Argentina",
    ciudad="Bariloche",
    descripcion="Aeropuerto Internacional Teniente Luis Candelaria",
)

ahora = datetime.now()

vuelo_cordoba = Vuelo(
    origen="Buenos Aires",
    destino="Cordoba",
    tipodeavion="Boeing 737",
    puertaembarque="A12",
    fechayhoravuelo=ahora + timedelta(days=7),
    telefonopasajero="3514449832"
)

vuelo_bariloche = Vuelo(
    origen="Buenos Aires",
    destino="Bariloche",
    tipodeavion="Airbus A320",
    puertaembarque="B5",
    fechayhoravuelo=ahora + timedelta(days=10),
    telefonopasajero="3514449832"
)

