from django_registration.forms import RegistrationForm
from django_registration.forms import RegistrationFormUniqueEmail
from django_registration.forms import RegistrationFormTermsOfService
from main.models import User

class UserForm(RegistrationFormUniqueEmail, RegistrationFormTermsOfService):
    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User
        fields = ['username','email', 'first_name','last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'placeholder': "الاسم الأول"})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'placeholder': "كلمة المرور"})
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'placeholder': "اسم المستخدم"})
        self.fields['birth_date'].widget.attrs.update({'class' : 'form-control', 'placeholder': "تاريخ الولادة"})
        self.fields['email'].widget.attrs.update({'input type' : 'text', 'class' : 'form-control', 'placeholder': "البريد الإلكتروني"})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'placeholder': "اسم العائلة"})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control', 'placeholder': "تأكيد كلمة المرور"})