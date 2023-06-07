from django import forms
from snack.models import Snack


class RequestForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Snack
        fields = ['name', 'image', 'url', 'description']
        labels ={
            'name': '신청할 간식 이름',
            'image': '간식의 사진',
            'url': '구매 사이트 주소',
            'description': '개수 등 설명 추가'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }