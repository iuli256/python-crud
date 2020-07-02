from django.forms import ModelForm
from restaurants.models import Product, NutritionalValues


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'status']

class NutritionalValuesForm(ModelForm):
    class Meta:
        model = NutritionalValues
        fields = ['product', 'nutritional_type', 'nutritional_value']
