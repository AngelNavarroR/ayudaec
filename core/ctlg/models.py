import logging
from os import path

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.search import SearchVectorField, SearchQuery, SearchRank
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from geopy.geocoders import Nominatim
from simple_history.models import HistoricalRecords

from core.utils import create_thumbnail, rename_img


logger = logging.getLogger(__name__)
THUMBNAIL_BASEWIDTH = 500

class provincias(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        "Nombre Provicia",
        max_length=100,
        help_text="Nombre de Provincia"
    )
    lat = models.FloatField("Latitud", help_text="Coordenada Y")
    lngt = models.FloatField("Longitud",help_text="Coordenada X")


class ciudades(models.Model):
    id = models.AutoField(
        primary_key=True,

    )
    name = models.CharField(
        "Nombre Ciudad",
        max_length=100,
        help_text="Nombre de Ciudad"
    )
    lat = models.FloatField("Latitud", help_text="Coordenada Y")
    lngt = models.FloatField("Longitud",help_text="Coordenada X")
