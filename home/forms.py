from django.forms import ModelForm
from .models import Order
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['ordered_at','customer_name']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
