from django.forms import ModelForm
from models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
