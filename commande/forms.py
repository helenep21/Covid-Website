from .models import Produit, Commande, Article
from django import forms
#from django.forms import ModelForm



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['produit', 'quantite']


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['produit', 'quantite']
        
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nomProduit', 'description']