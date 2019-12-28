from django_registration.forms import RegistrationForm
from django_registration.forms import RegistrationFormUniqueEmail
from django_registration.forms import RegistrationFormTermsOfService



from main.models import User

class UserForm(RegistrationFormUniqueEmail, RegistrationFormTermsOfService):
    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User
        fields = ['username','email', 'first_name','last_name', 'birth_date']