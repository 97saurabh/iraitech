from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):



    class Meta:
        fields=('email','password1','first_name','last_name','phone_number')
        model=get_user_model()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['email'].label = "Email Address"
        self.fields['first_name'].label = "Your Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['phone_number'].label = "Phone No"
    

