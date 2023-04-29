from django import forms

from app.models import *

class Topicform(forms.ModelForm):

    class Meta():
        model=Topic
        fields='__all__'
        help_texts={'topic_name':'Maximum length is 10-characters'}

class Webpageform(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        help_texts={'name':'minimum length is FIVE'}


class Accessrecordform(forms.ModelForm):
    class Meta():
        model=Accessrecord
        fields='__all__'
        help_texts={'date':'dtae formate is YYYY-MM-DD','author':'min char is 5 and max is 10'}