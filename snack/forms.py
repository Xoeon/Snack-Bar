from django import forms
from snack.models import Snack


class RequestForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Snack
        fields = ['name', 'image', 'url', 'description']
        labels ={
            'name': '신청할 간식 이름',
            'url': '구매 사이트 주소',
        }