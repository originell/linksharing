from django.forms import ModelForm
from models import Link

class LinkForm(ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.user = request.user
        super(LinkForm, self).__init__(*args, **kwargs)
        
    def save(self, commit=True):
        obj = super(LinkForm, self).save(commit=False)
        obj.author = self.user
        if commit:
            obj.save()
        return obj
        
    class Meta:
        model = Link
