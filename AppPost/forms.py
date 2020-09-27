from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description')

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=25, required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)