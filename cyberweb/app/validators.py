from django.core.validators import ValidationError
def file_image(value):
    if not str(value).endswith('.jpg'):
        raise ValidationError('файл не того типа')

