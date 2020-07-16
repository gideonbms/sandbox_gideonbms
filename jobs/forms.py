from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'username',
            'Email',
            'subject',
            'feedback'
        ]


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'user','title', 'company_name', 'employment_status', 'vacancy', 'category',
            'description', 'responsibilities', 'experience', 'job_location', 'Salary',
            'image', 'application_deadline', 'published_on'
        ]


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        widgets ={
            'image': forms.HiddenInput(),
            'education': forms.HiddenInput(),
            'experience': forms.HiddenInput(),
            'location': forms.HiddenInput(),
            'bio': forms.HiddenInput(),
        }
        fields = [
            'name', 'education', 'experience', 'location', 'image', 'bio'
        ]

class LogForm(forms.ModelForm):
    class Meta:
        model = UserLog
        fields = [
            'passcode',
        ]