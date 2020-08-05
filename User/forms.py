from  django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        # fields = '__all__'
        fields = ('first_name','last_name','username','email','password1','password2')

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields ='__all__'


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['first_name','last_name','email','username','password1','password2','is_customer']

