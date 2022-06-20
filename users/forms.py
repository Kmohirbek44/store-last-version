from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import myauth


class authforuser(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ismingizni kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'parolni kiriting'}))
    class Meta:
        model=myauth
        fields=('username','password')
    def __init__(self,*args,**kwargs):
        super(authforuser, self).__init__(*args,**kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class']='form-control py-4'
class register(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ismingizni kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'familangizni kiriting'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'emailni kiriting'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usernameni kiriting'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni qaytadan kiriting'}))
    class Meta:
        model=myauth
        fields=('first_name','last_name','email','username','password1','password2')
    def __init__(self,*args,**kwargs):
        super(register, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
class profile(UserChangeForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'readonly':True}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'readonly':True}))
    image=forms.ImageField(widget=forms.FileInput(),required=False)
    class Meta:
        model=myauth
        fields=('first_name','last_name', 'email','username','password','image')

    def __init__(self, *args, **kwargs):
        super(profile, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class']='custom-file-input'
