from django.core.validators import ValidationError
from random import randint


def file_image(value):
    if not str(value).endswith('.jpg'):
        raise ValidationError('файл не того типа')


def random_uuid():
    uuid = "".join(map(str,[randint(0, 9) for el in range(10)]))
    return uuid
