from django import forms

from apps.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'about', 'email', 'phone', 'password']




    def clean_password_confirm(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data['password_confirm']



