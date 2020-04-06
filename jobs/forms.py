from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
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
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'web', 'education', 'experience', 'location', 'cv_file', 'resume'
        ]