from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from location_field.models.plain import PlainLocationField


gender_choices = [
    ('male', 'ذكر'),
    ('female', 'أنثى')
]


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True,
                              validators=[EmailValidator(message="your custom message")])
    birth_date = models.DateField(null=True, blank=True, verbose_name = 'تاريخ الميلاد')

    city = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True)
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        verbose_name = 'الجنس'
        )




