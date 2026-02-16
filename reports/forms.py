from django import forms
from .models import Report


class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ["created_at"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
