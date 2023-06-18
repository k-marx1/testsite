from django import forms
from .models import *


class AddProduct(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AddProduct, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    product_name = forms.CharField(max_length=255, widget=forms.TextInput())
    slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    in_stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Nothing', widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.FloatField()
    discount = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], )
    rating = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], required=False)
    available = forms.ChoiceField(required=False, initial=True)

