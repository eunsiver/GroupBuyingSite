from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name","password1", "password2", "email")

#회원정보 수정할 때
class editInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

# PasswordChangeForm2 추가 (5.27) -> 근데 안쓸듯?
class PasswordChangeForm2(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm2, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Old Password'
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password1'].widgets.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].label = 'Confirm New Password'
        self.fields['new_password2'].widgets.attrs.update({'class': 'form-control'})

