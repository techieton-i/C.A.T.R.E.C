from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User, validate_reg, UserProfile, ContactForm
from django import forms
from . import constants as user_constants


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name', 'autofocus': True, }))
    last_name = forms.CharField(max_length=20, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name', 'autofocus': True, }))
    reg_number = forms.CharField(max_length=12, validators=[validate_reg], required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Input your registration number',
                                                               'autofocus': True, }))
    user_type = forms.ChoiceField(choices=user_constants.USER_TYPE_CHOICES, required=True,
                                  widget=forms.Select(attrs={'class': 'bootstrap-select'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name', 'reg_number',
                  'user_type', 'password1', 'password2', )


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'user_type', )


class AdminCustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'user_type', )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=False, widget=forms.PasswordInput)
    new_password1 = forms.CharField(required=False, widget=forms.PasswordInput)
    new_password2 = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2', )


class EditProfileInfo(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('phone',
                  'sex',
                  'date_of_birth',
                  'is_verified')


class PostContactForm(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ('sender_email', 'sender_full_name', 'message', )


# Next actions - forgot password, edit profile, inject profile, admin reg issue
