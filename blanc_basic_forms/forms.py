from django import forms
from django.conf import settings


ANTI_SPAM = getattr(settings, 'FORMS_ANTISPAM', 'human')


class BasicForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.widgets.Textarea)
    anti_spam = forms.RegexField(
            regex='^(?i)%s$' % (ANTI_SPAM,),
            help_text='Please enter <strong>%s</strong> in the field above' %
            (ANTI_SPAM,))
