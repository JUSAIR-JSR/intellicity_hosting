from django import forms
from .models import Profile, Skill

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

class BannerImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['banner_image']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['certifications', 'qualifications', 'location']

class SkillSelectionForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Profile
        fields = ['skills']


# users/forms.py

from django import forms
from django.contrib.auth.models import User

class UsernamePasswordUpdateForm(forms.Form):
    new_username = forms.CharField(
        max_length=150, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'New Username'})
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}), 
        required=False
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), 
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if password fields are filled and match
        if new_password and confirm_password:  # Password fields must match if provided
            if new_password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
