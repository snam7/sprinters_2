
from django import forms
from .models import MenuItem,Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'image', 'is_available', 'chef']
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivered']