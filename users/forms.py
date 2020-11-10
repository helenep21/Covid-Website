from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Adresse e-mail")
    phone = forms.CharField(max_length=12, label='N° de téléphone')
    address = forms.CharField(max_length=80, label='Rue et numéro')
    city = forms.CharField(max_length=80, label='Ville')
    country = forms.CharField(max_length=80, label='Pays')
    nbp = forms.IntegerField(max_value=15, label_suffix="Nombre d'habitants")
    noms = forms.CharField(
        max_length=400, label="Noms de chaque habitant (séparés d'une virgule)")
    prenoms = forms.CharField(
        max_length=400, label="Prénoms de chaque habitant (séparés d'une virgule et dans le même ordre qu'au dessus")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'city',
                  'country', 'nbp', 'noms', 'prenoms', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        personne = Profile(user=user, phone=self.cleaned_data['phone'], address=self.cleaned_data['address'], city=self.cleaned_data['city'],
                           country=self.cleaned_data['country'], nbp=self.cleaned_data['nbp'], noms=self.cleaned_data['noms'], prenoms=self.cleaned_data['prenoms'])
        if commit:
            user.save()
            personne.save()
        return user
