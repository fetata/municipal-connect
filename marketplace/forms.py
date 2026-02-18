from django import forms
from .models import MarketplaceItem


class MarketplaceCreateForm(forms.ModelForm):
    class Meta:
        model = MarketplaceItem
        exclude = ["created_at"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
