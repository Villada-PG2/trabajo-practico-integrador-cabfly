from datetime import datetime, timedelta

from modelos import (
    Asiento,
    CambioReserva,
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


# usuarios y pasajeros

usuario = Usuario(
    nombrecompleto="Juan Perez",
    dni="12345678",
    mail="juan.perez@gmail.com",
    telefono="3514449832",
    contraseña="juanperez1990"
)


pasajero_1 = Pasajero(
    nombre="Juan",
    dni= "09876543",
    telefono="3516785432",
    mail="juan.perez@gmail.com"
)


pasajero_2 = Pasajero(
    nombre="Daniela",
    dni="32165487",
    telefono="3512223689",
    mail="daniela@gmail.com"
)


#ej uso

reserva_juan = Reserva(
    vueloprogramado=vuelo_cordoba,
    montototal=355550.00
)
print(reserva_juan.generarReserva())

asiento_juan = Asiento(tipoasiento="Ventanilla", numeroasiento="A04")
print(f"Selección: {asiento_juan.elegirAsiento()}")

pago_juan = Pago(
    tipotarjeta="Mastercard",
    infotarjeta="1111222233334444",
    infopago="Pago aprobado en un unico pago",
)
pago_juan.confirmarReserva()
print(f"Estado despues del pago: {reserva_juan.estadoReserva}")

tarjeta_juan = TarjetaEmbarque(
    datosPasajero=pasajero_1,
    codigoqr="QR-COR-2026-004",
    numeroasiento=asiento_juan.numeroasiento,
    vuelo=vuelo_cordoba
)

lista_reservas = []
lista_reservas.append(
    {
        "reserva": reserva_juan,
        "pasajero": pasajero_1,
        "asiento": asiento_juan,
        "tarjeta": tarjeta_juan

    }
)


#reserva daniela

reserva_daniela = Reserva(
    vueloprogramado=vuelo_bariloche,
    montototal=555000,
)
print(reserva_daniela.generarReserva())


asiento_daniela = Asiento(tipoasiento= "Pasillo", numeroasiento="C12")
print(f"Seleccion: {asiento_daniela.elegirAsiento()}")


vuelo_bariloche_nuevo = Vuelo(
    origen="Buenos Aires",
    destino="Bariloche",
    tipodeavion="Airbus 320",
    puertaembarque="A12",
    fechayhoravuelo=ahora + timedelta(days=22),
    telefonopasajero="3512223689"
)


cambio = CambioReserva(
    nuevafecha=str(vuelo_bariloche_nuevo.fechayhoravuelo),
    infonuevovuelo="Reprogramacion por trabajo",
    vuelo=vuelo_bariloche_nuevo,
)

reserva_daniela.reprogramarVuelo(vuelo_bariloche_nuevo)
print("Vuelo reprogramado exitosamente")

tarjeta_daniela = TarjetaEmbarque(
    datosPasajero=pasajero_2,
    codigoqr="QR-BRC-2026-088",
    numeroasiento=asiento_daniela.numeroasiento,
    vuelo=vuelo_bariloche_nuevo,
)

lista_reservas.append(
    {
        "reserva": reserva_daniela,
        "pasajero": pasajero_2,
        "asiento": asiento_daniela,
        "tarjeta": tarjeta_daniela
    }
)