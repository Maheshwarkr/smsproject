import pytz
from django import forms
from .models import Task, Feedback
from .models import StudentList
from .models import Feedback
from .models import Contact

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'maxlength': 150}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.EmailField().clean(email):
            raise forms.ValidationError("Please enter a valid email address.")
        return email







from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']

class EmailForm(forms.Form):
    recipient_email = forms.EmailField(label="Send to Email")