
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class Usuario(BaseModel):
    nombrecompleto: str
    dni: str = Field(...,min_length=8, max_length=8)
    mail: EmailStr
    telefono: str = Field(...,min_length=10, max_length=10)
    contraseña: str = Field(...,min_length=8)


class Vuelo(BaseModel):
    origen: str 
    destino: str
    telefonopasajero: str = Field(...,min_length=10, max_length=10)
    tipodeavion: str 
    puertaembarque: str = Field(min_length=1, max_length=10)
    fechayhoravuelo: datetime


class Reserva(BaseModel):
    vueloprogramado: Vuelo
    fechacreacion: datetime = Field(default_factory=datetime.now)
    montototal: float = Field(..., gt=0)
    estadoReserva: str = Field(default="Pendiente")

    def generarReserva(self):
        self.estadoReserva = "CONFIRMADA"
        return f"Reserva generada. Estado: {self.estadoReserva}, Fecha de creación: {self.fechacreacion}, Monto total: {self.montototal}"

    def verificarVigencia(self):
        return self.vueloprogramado.fechayhoravuelo > datetime.now()

    def reprogramarVuelo(self, nuevo_vuelo: Vuelo):
        self.vueloprogramado = nuevo_vuelo


class CambioReserva(BaseModel):
    nuevafecha: str = Field(..., min_length=8)
    infonuevovuelo: str = Field(..., max_length=100)
    vuelo: Vuelo


class Destino(BaseModel):
    pais: str = Field(..., min_length=2, max_length=50)
    ciudad: str = Field(..., min_length=2, max_length=50)
    descripcion: str = Field(..., min_length=20, max_length=400)


class Asiento(BaseModel):
    tipoasiento: str = Field(..., min_length=3, max_length=10)
    numeroasiento: str = Field(pattern=r"^[A-Z][0-9]{2}$")

    def elegirAsiento(self):
        return f"Asiento {self.numeroasiento} ({self.tipoasiento} seleccionado)"


class Pasajero(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    dni: str = Field(...,min_length=8, max_length=8)
    telefono: str = Field(...,min_length=10, max_length=10)
    mail: EmailStr


class Pago(BaseModel):
    tipotarjeta: str = Field(..., min_length=3, max_length=20)
    infotarjeta: str = Field(..., min_length=16, max_length=16, pattern=r"^[0-9]{16}$")
    infopago: str = Field(..., max_length=100)

    def pagar(self):
        return f"Pago realizado con tarjeta {self.tipotarjeta}. Información de pago: {self.infopago}"

    def confirmarReserva(self):
        Reserva.estadoReserva = "Pagado"


class TarjetaEmbarque(BaseModel):
    datosPasajero: Pasajero
    codigoqr: str = Field(..., min_length=10)
    numeroasiento: str = Field(..., pattern=r"^[A-Z][0-9]{2}$")
    vuelo: Vuelo
