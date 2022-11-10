from django.forms import ModelForm
from .models import person, laptop


class addPerson(ModelForm):
    class Meta:
        model  = person
        fields = '__all__'
