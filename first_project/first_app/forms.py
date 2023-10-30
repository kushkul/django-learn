from django.forms import ModelForm
from first_app.models import User


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']




        
