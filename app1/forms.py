from django import forms
from app1.models import *
class Sch(forms.ModelForm):
    class Meta:
        model=SchoolInfo
        #fields='__all__' #It is used for creating the input elements for all the columns
        fields=['scname','sclocation'] #if i want input elements for only menctioned colums
        #exclude=['sclocation']#except that menctioned column exclude will create the input elements for remaining columns
        help_texts={'sclocation':'enter school location'} #documetation purpose
        labels={'scname':'school name','sclocation':'school location'}#If i want to display the input element actual name to particular name


class Std(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields='__all__'
        #widgets={'subjects':forms.RadioSelect}#if i want to display the parent column input data in the form of radio button and by default it is an drop down box
        widgets={'subjects':forms.RadioSelect,'age':forms.PasswordInput,'stlocation':forms.Textarea}
        