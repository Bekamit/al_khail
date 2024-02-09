from apps.staticdata.models import Body
from django.db import models


def check_charfield_lengths():

    instance = Body.get_solo()
    fields = Body._meta.get_fields()

    for field in fields:
        if isinstance(field, models.CharField):

            value = getattr(instance, field.attname)
            max_length = field.max_length

            if len(value) > max_length:
                print(
                    f"Error: The value '{value}' in field '{field.name}' exceeds the maximum length of {max_length} characters.")
