from django import forms


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(
        label="Rating",
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(
            attrs={
                "class": "rounded-md",
            }
        ),
    )
    user_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"class": "rounded-md"}),
    )
    product_id = forms.IntegerField(
        label="",
        widget=forms.HiddenInput(),
    )
    text = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={
                "class": "rounded-md",
                "rows": 3,
                "cols": 10,
            }
        ),
    )
