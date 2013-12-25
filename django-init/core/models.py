# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import User

from utils_django_init.models import BaseModel


class Persona(BaseModel):
    """
    This model represent a person.

    Contains person information related with system.

    """
    GENERO = (
        ('F', u'Femenino'),
        ('M', u'Masculino'),
        ('O', u'Otro')
    )
    nombre = models.CharField(u'Nombre', max_length=255)
    apellido = models.CharField(u'Apellido', max_length=255)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento', help_text="DD/MM/AAAA")
    genero = models.CharField(u'Género', max_length=1, choices=GENERO, default=u'F')
    estado_civil = models.CharField(u'Estado civíl', max_length=255, default=u'soltero')
    dni = models.IntegerField(u'DNI')
    domicilio = models.CharField(u'Domicilio', max_length=255, blank=True)
    observaciones = models.TextField(u'Observaciones', blank=True)
    # relationship
    # contacto = models.ForeignKey(Contacto, verbose_name=u'Contacto', null=True)
    # profesion = models.ForeignKey(Profesion, verbose_name=u'Profesión', null=True)

    def __unicode__(self):
        return u"{} {}".format(
                self.nombre, self.apellido)

    class Meta:
        verbose_name = u"persona"
        verbose_name_plural = u"personas"
