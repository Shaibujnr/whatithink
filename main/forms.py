from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,
                                   max_length=100,
                                   widget=forms.TextInput(attrs={
                                       'class':'form-control',
                                       'id': "tcname",
                                       'placeholder':"Your Name",
                                       'data-rule':'minlen:4',
                                       'data-msg':'please enter at least 4 chars'

                                   }))

    contact_email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={
                                         'class': 'form-control',
                                         'id': 'contact_email',
                                         'placeholder':'Your Email',
                                         'data-rule': 'email',
                                         'data-msg': 'Please enter a valid email'
                                     }))

    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={
                                  'class':'form-control',
                                  'id': 'subject',
                                  'placeholder': 'Subject',
                                  'data-rule':'minlen:4',
                                  'data-msg': 'Please Enter at least 8 chars of subject'
                              }))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={
                                  'class':'form-control',
                                  'rows':'5',
                                  'id':'message',
                                  'data-msg':'please write something for us',
                                  'placeholder': 'Message'
                              }))

