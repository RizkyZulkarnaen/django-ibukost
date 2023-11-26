from django import forms
from django.forms import ModelForm
from .models import kost_member, user_member
from django.forms import TextInput, Textarea, Select

class user_form(ModelForm):
    class Meta:
        model = user_member
        fields = [
            'username',
            'tag_id',
            'unique_id',
            'telepon',
            'alamat',
        ]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control textInput',
                'placeholder': 'Jhon Kenedy'
                }),
            'tag_id': TextInput(attrs={
                'class': 'form-control textInput',
                'placeholder': 'xxx-xxx-xxx',
                'type': 'number'
                }),
            'unique_id': TextInput(attrs={
                'class': 'form-control textInput',
                'placeholder': 'xxxx',
                'type': 'number'
                }),
            'telepon': TextInput(attrs={
                'class': 'form-control textInput',
                'placeholder': '821-xxxx-xxxx',
                'type': 'number'
                }),
            'alamat': Textarea(attrs={
                'class': 'form-control textArea'}),
        }

class kost_form(ModelForm):
    class Meta:
        model = kost_member
        fields = [
            'nama_kost',
            'nomor_kost',
            'unique_id',
            'status',
        ]
        
        widgets = {
            'nama_kost': TextInput(attrs={
                'class' : 'form-control textInput',
                'placeholder' : 'Kost Pelita'
                }),
            'nomor_kost': TextInput(attrs={
                'class' : 'form-control textInput',
                'placeholder' : 'A80'
                }),
            'unique_id': TextInput(attrs={
                'class' : 'form-control textInput',
                'placeholder' : 'xxxx',
                'type' : 'number'
            }),
            'status': Select(attrs={
                'class' : 'form-control selectInput',
            }),
        }