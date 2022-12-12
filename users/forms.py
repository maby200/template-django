from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        '''Indicar que este form pertenece a un modelo'''
        model = User
        ''' Podemos definir qué campos seran mostrados usando el atributo fields '''
        fields = ['username', 'first_name','last_name','email','password1','password2']

    
    ''' sobreescribir el metodo save'''

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email
        user.email = self.cleaned_data['email']
        if commit : 
            user.save()
        return user