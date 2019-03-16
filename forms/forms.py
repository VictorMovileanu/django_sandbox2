from django import forms
from .models import ProductModel


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = '__all__'


class StyledForm(forms.Form):
    first_name = forms.CharField(max_length=20, help_text='last name')
    last_name = forms.CharField(max_length=20, help_text='first name')
    email = forms.CharField(max_length=20, help_text='email')
