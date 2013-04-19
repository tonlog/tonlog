from django import forms

TOPIC_CHOICES = (
    ('A','a'),
    ('B','b'),
    ('C','c'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(), initial="input your ideas..")
    sender  = forms.EmailField(required=False,)
