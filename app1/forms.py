from django import forms
from app1.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
class AccessRecord(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'