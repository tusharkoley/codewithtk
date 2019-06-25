from django import  forms
    
class ContactForm(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    widgets = {
            
            'message': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class NotificationForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)