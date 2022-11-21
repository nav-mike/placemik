from django import forms

from webapp.models.category_group import CategoryGroup


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


class TextSearchForm(forms.Form):
    categoryGroup = forms.ChoiceField(
        label="",
        choices=[(0, "All categories")]
        + [(group.id, group.name) for group in CategoryGroup.objects.all()],
        widget=forms.Select(
            attrs={
                "class": "border-0 h-full bg-purple-100",
            }
        ),
    )
    search = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search",
                "class": "flex-1 focus:outline-0 px-4 border-0",
            }
        ),
    )
