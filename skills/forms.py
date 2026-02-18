from django import forms
from .models import Skill


class SkillCreateForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["created_at"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
