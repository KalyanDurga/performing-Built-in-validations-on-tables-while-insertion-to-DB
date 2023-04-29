from django.db import models

# Create your models here.
from django.core import validators

class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True,validators=[validators.MaxLengthValidator(10)])

    def __str__(self) -> str:
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=10,validators=[validators.MinLengthValidator(5)])
    url=models.URLField(validators=[validators.URLValidator()])
    Email=models.EmailField(validators=[validators.EmailValidator()])

    def __str__(self) -> str:
        return self.name
    
class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=50,validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(10)])
    date=models.DateField()


    def __str__(self) -> str:
        return self.author