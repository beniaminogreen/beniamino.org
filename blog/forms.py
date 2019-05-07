from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=False)
    name = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea(attrs={'size': 20}), required=True)
    
