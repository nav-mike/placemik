from django import forms

from webapp.models.order import Order


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


class OrderForm(forms.ModelForm):
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
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "rounded-md",
                "rows": 3,
                "cols": 10,
            }
        ),
    )

    class Meta:
        model = Order
        fields = [
            "user_name",
            "user_email",
            "user_phone",
            "user_address",
            "user_comment",
        ]
