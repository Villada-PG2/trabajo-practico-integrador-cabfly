# Analisis de Requerimientos - CabFly (Aerolinea)

## Entradas
1. Datos del usuario: nombre, apellido, mail, telefono, dni.
2. Criterios de busqueda: ciudad de origen, destino, cantidad de pasajeros, fecha de salida / vuelta.
3. Datos de pasajeros: nombre, apellido, dni o pasaporte, mail, telefono
4. Selección de asiento
5. Datos de pago: tipo de tarjeta, informacion de tarjeta (titular, codigo, número, fecha de vencimiento)

## Salidas
1. Listado de vuelos disponibles: vuelos que coincidan con la busqueda del usuario
2. Mapa de asientos: muestra asientos disponibles para elegir
3. Comprobante de pago
4. Tarjeta de embarque



## Frontera
1. Control en el aeropuerto de los pasajeros (chequeo de pasajes, pasaporte, equipaje, etc)
2. Asignación de la puerta de embarque específica dentro del aeropuerto
3. Cumplimiento de leyes fiscales


## Alcance
#1. Gestion de usuarios
1.1 Permitir el registro de nuevos usuarios 

#2. Busqueda de vuelos
2.1 Permitir buscar vuelos disponibles según criterios ingresados
2.2 Mostrar listado de vuelos que coincidan con los criterios

#3. Reserva
3.1 Permitir al usuario registrar datos de los pasajero
3.2 Seleccion de asientos con el mapa interactivo
3.3 Calcular el costo de la reserva 
3.4 Generar codigo de reserva 
3.5 Verificar vigencia de reserva (regla de 48 horas para el pago)

#4. Pago
4.1 Permitir el registro de datos de pago (tipo de tarjeta y datos)
4.2 Actualizar el estado de la reserva (pagado)
4.3 Generar tarjeta de embarque para los pasajeros
4.4 Enviar un mail a los pasajeros con la tarjeta de embarque

#5. Reprogramacion
5.1 Permitir la reprogramacion de una reserva
5.2 Mostrar vuelos disponibles para reprogramar
5.3 Calcular la diferencia de precios entre la reserva original y el nuevo vuelo
5.4 Emitir la nueva tarjeta de embarque con los datos actualizados