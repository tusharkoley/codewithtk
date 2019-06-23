
from django import forms

from .models import Edge


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Edge
        fields = ['image']