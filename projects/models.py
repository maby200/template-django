from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    #hacer que agarre automaticamente el usuario que ha iniciado sesion:
    user = models.ForeignKey(User, on_delete=models.CASCADE) #, default=User.username
    # Pillow is needed:
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics') 
    title = models.CharField(max_length=250,default='project title')
    description = models.TextField(default='Another project')
    tags = models.CharField(max_length=250,default='html, css, django')
    link = models.URLField(default='https://github.com/maby200/')


    # https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
    # ip_address = models.CharField(max_length=15, default='127.0.0.1')

    def __str__(self) -> str:
        return f'{self.user.username} portfolio project'