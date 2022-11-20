from django import forms


class NewsletterForm(forms.Form):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email here",
                "class": "max-w-sm w-96 bg-transparent border-white placeholder-white placeholder:italic",
            }
        ),
    )
