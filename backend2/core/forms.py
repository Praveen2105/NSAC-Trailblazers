from django import forms
from .models import UserReport


class UserReportForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = '__all__'