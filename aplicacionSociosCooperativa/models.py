from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Socio (models.Model):
    documento = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    correo = models.CharField(max_length=50, blank=True)
    curso = models.CharField(max_length=10, blank=False)
    fechaInscripcion = models.DateField()
    completo = 1
    incompleto = 0
    estadoSocio = (
        (completo,"completo"),
        (incompleto,"incompleto")
        )
    socioCompleto = models.IntegerField(choices=estadoSocio,default=incompleto)
    usuarioCampus = models.CharField(max_length=50,blank=True)
    ninguna = 0
    informatica = 1
    electronica = 2
    opcionesEspecialidad = (
        (ninguna,"ninguna"),
        (informatica,"informatica"),
        (electronica,"electronica")
        )
    epecialidad=models.IntegerField(choices=opcionesEspecialidad,default=ninguna)
    fechaNacimiento = models.DateField()

    def __str__ (self):
        return str(self.documento)+' | '+self.nombre+' '+self.apellido

class Pago(models.Model):
    soloNaturales = RegexValidator(r'^[0-9]*')
    socio = models.ForeignKey('Socio')
    fecha = models.DateField(blank=False,null=False)
    pago = models.IntegerField(blank=False,null=False, validators=[soloNaturales])

    def __str__ (self):
        return str(self.fecha)+' ! $'+str(self.pago) + " "+ self.socio.nombre + " " + self.socio.apellido

class Importe(models.Model):

    fechaInicio = models.DateField(blank=False,null=False)
    fechaFin = models.DateField(blank=False,null=False)
    coste = models.IntegerField(blank=False,null=False)

    def __str__ (self):
        return str(self.fechaInicio)+' - '+str(self.fechaFin)+' | $'+str(self.coste)

