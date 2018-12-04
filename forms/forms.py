from django.forms import ModelForm
from .models import ProductModel


class ProductForm(ModelForm):

    class Meta:
        model = ProductModel
        fields = '__all__'
