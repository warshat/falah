from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField


gender_choices = [
    ('male', 'ذكر'),
    ('female', 'أنثى')
]


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True,
                              validators=[EmailValidator(message="your custom message")])
    birth_date = models.DateField(null=True, blank=True, verbose_name = 'تاريخ الميلاد')

    city = models.CharField(max_length=255, null=True, verbose_name = 'المدينة')
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True, verbose_name = 'الموقع')
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        verbose_name = 'الجنس'
        )
    photo = models.ImageField(upload_to='./media/profile_pics', height_field=None, width_field=None, blank=True, verbose_name = 'صورة شخصية')

    phone_number = PhoneNumberField(blank=True, verbose_name = 'رقم الهاتف')
    


class Service(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name = 'المهنة')
    description = models.CharField(max_length=255, null=True, verbose_name = 'وصف المهنة')
    thumbnail = models.ImageField(upload_to='./media/service_thumbnails', height_field=None, width_field=None, blank=True, verbose_name = 'صورة توضيحية')
    