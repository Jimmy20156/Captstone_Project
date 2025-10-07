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
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
