from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'cover_letter', 'resume_url', 'linkedin_url', 'portfolio_url']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (optional)'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Tell us about yourself and why you want to join Jovian...'}),
            'resume_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link to your resume (Google Drive, Dropbox, etc.)'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn Profile URL (optional)'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Portfolio / GitHub URL (optional)'}),
        }
