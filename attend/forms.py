from django import forms
from .models import SaveImage
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = SaveImage
        fields = ("name", "image")