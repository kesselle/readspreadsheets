from django import forms
from . models import Product, Customer



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item', 'quantity', 'amount', 'date']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= ['first_name', 'last_name', 'email', 'gender', 'date']
