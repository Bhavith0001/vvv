
from django.core.exceptions import ValidationError

def validate_image_size(file):
    max_image_size = 500

    if file.size > max_image_size*1024:
        raise ValidationError(f'File cannot be larger than {max_image_size}kb.')