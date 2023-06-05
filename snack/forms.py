from django import forms
from snack.models import Snack


class RequestForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Snack
        fields = ['name', 'image', 'url']