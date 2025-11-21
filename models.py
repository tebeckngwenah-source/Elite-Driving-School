from django.db import models
from django.core.validators import MinLengthValidator
class Contact_user(models.Model):
    username = models.CharField(max_length=10,validators=[MinLengthValidator(4)])
    email = models.EmailField()
    message = models.TextField(validators=[MinLengthValidator(10)])
# Create your models here.
