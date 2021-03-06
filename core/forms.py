from selectors import SelectSelector

from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.safestring import mark_safe
from leaflet.forms.fields import PointField

from .models import HelpRequest


class HelpRequestForm(forms.ModelForm):
    location = PointField(
        label="Ubicación:",
        error_messages={'required': mark_safe('Te olvidaste de marcar tu ubicación en el mapita\n <br>Si tienes un problemas con este paso \
            <a href="#" class="is-link modal-button" data-target="#myModal" aria-haspopup="true">mira esta ayuda</a></p>\
            <p id="div_direccion" style="font-size: 10px; margin-bottom: 5px;"></p>')},
        help_text=mark_safe('<p style="margin-bottom:5px;font-size:10px;">Selecciona tu Ubicación para que las personas solidarias te puedan encontrar.\
            <br>Si tienes un problemas con este paso \
                <a href="#" class="is-link modal-button" data-target="#myModal" aria-haspopup="true">mira esta ayuda</a></p>\
                <p id="div_direccion" style="font-size: 10px; margin-bottom: 5px;"></p>'),
    )

    class Meta:
        model = HelpRequest

        fields = (
            "title",
            "message",
            "categories",
            "name",
            "phone",
            "provincia",
            "location",
            "address",
            "picture"
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ejemplo: Necesito de manera urgente víveres para mi familia",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "textarea",
                    "rows": 4,
                    "placeholder": "Puedes describir detalladamente lo que necesites, ",
                }
            ),
            "name": forms.TextInput(attrs={"class": "input"}),
            "phone": forms.TextInput(attrs={"class": "input", "type": "tel"}),
            "address": forms.TextInput(attrs={"class": "input"}),
            'categories': forms.SelectMultiple(attrs={"style": "display:none;"}),
            "provincia": forms.Select(attrs={"id": "provicia_id",
                    "placeholder": "Seleccione una provincia"}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Registro ya ingresado, no puede duplicar mismo pedido.",
            }
        }
