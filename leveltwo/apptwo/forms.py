from django import forms
from apptwo.models import Users
class New_userForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'