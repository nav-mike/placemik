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
    product = forms.IntegerField(
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


class OrderForm(forms.Form):
    user_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"class": "rounded-md"}),
    )
    user_email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "rounded-md"}),
    )
    user_phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(attrs={"class": "rounded-md"}),
    )
    user_address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={"class": "rounded-md"}),
    )
    user_comment = forms.CharField(
        label="Comment",
        widget=forms.Textarea(
            attrs={
                "class": "rounded-md",
                "rows": 3,
                "cols": 10,
            }
        ),
    )
