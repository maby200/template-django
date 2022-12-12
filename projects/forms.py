from django import forms
from .models import Portfolio

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'user',
            'photo',
            'title',
            'description',
            'tags',
            'link',
        ]