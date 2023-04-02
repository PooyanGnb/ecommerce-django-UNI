from django import forms
from shop.models import Product, Contact, NewsLetter
# from captcha.fields import CaptchaField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']


class ImageForm(ProductForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ['images',]


class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    
    class Meta:
        model = Contact
        fields  = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'