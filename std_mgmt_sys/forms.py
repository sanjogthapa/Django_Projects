from django import forms
from django.forms import Form, ModelForm
from std_mgmt_sys.models import Tutorials, Books, Students


class AddBooksForm(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    published_date = forms.IntegerField()
    price = forms.IntegerField()



class TutorialsModelForm(forms.ModelForm):
    class Meta:
        model= Tutorials
        fields=('subject', 'teacher', 'date_submission')


class AddBooksModelForm(forms.ModelForm):
    class Meta:
        model= Books
        fields = ('name', 'author', 'published_date', 'price', 'profile_photo')



class AddStudentsModelform(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('name', 'roll')