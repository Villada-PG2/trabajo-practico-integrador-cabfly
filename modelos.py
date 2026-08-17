from operator import gt

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


class Destino(BaseModel):
    pais: str = Field(..., min_length=2, max_length=50)
    ciudad: str = Field(..., min_length=2, max_length=50)
    descripcion: str = Field(..., min_length=20, max_length=400)


class Asiento(BaseModel):
    tipoasiento: str = Field(..., min_length=3, max_length=10)
    numeroasiento: str = Field(pattern=r"^[A-Z][0-9]{2}$")

    def elegirAsiento(self):
        return f"Asiento {self.numeroasiento} ({self.tipoasiento} seleccionado)"
    
