from django import forms


class ProfileForm(forms.Form):
    " forms for uploadtin profile picture"
    user_image = forms.ImageField(label="Profile Picture")
