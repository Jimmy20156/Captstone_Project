from django import forms
from django.contrib.auth.models import User, Group

ROLE_CHOICES = [
    ('Teachers', 'Teacher'),
    ('Students', 'Student'),
    ('Advisers', 'Adviser'),
]

class SignUpForm(forms.ModelForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Assign the user to a group after saving
            role = self.cleaned_data['role']
            group = Group.objects.get(name=role)
            user.groups.add(group)
        return user

class SignInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your username',
        }),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your password',
        }),
        label='Password'
    )