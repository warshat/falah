from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField


gender_choices = [
    ('male', 'ذكر'),
    ('female', 'أنثى')
]

class Rate(models.Model):
    rate = models.FloatField(default=0.0, verbose_name = 'التقييم')
    number_votes = models.IntegerField(default=0, verbose_name = 'عدد الأصوات')

    def vote(self, vote):
        self.rate = (self.rate * self.number_votes +
                     vote) / (self.number_votes+1)
        self.number_votes += 1
        return self.rate

    class Meta:
        abstract = True


class User(Rate, AbstractUser):
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

    registration_date = models.DateField(null=True, blank=True, verbose_name = 'تاريخ إنشاء الحساب')

    is_worker = models.BooleanField(blank=True, default=False)
    
    def __str__(self):
        str_value = self.first_name + self.last_name
        if len(str_value) < 1:
            str_value = self.username
        return str_value

class Worker(Rate):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        'Service',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name = 'المهنة',
    )

    def __str__(self):
        return self.user
    



class Service(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name = 'المهنة')
    description = models.CharField(max_length=255, blank=True ,null=True, verbose_name = 'وصف المهنة')
    thumbnail = models.ImageField(upload_to='./media/service_thumbnails', height_field=None, width_field=None, blank=True, verbose_name = 'صورة توضيحية')

    def __str__(self):
        return self.name
    

