from django import forms
from .models import JobPosting, Skill

class JobPostingForm(forms.ModelForm):
    application_deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )
    required_skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    new_skills = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter new skills separated by commas")
    
    class Meta:
        model = JobPosting
        fields = ['title', 'description', 'required_qualifications', 'required_skills', 'new_skills', 'location', 'application_deadline', 'job_post_image']



from django import forms
from .models import JobApplication


from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []  # No fields shown by default
    
    cv = forms.FileField(
        label='Upload Your CV',
        help_text='Accepted formats: PDF, DOC, DOCX (Max size: 5MB)',
        widget=forms.FileInput(attrs={
            'accept': '.pdf,.doc,.docx',
            'class': 'form-control-file',
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add additional initialization here if needed
    
    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        
        if not cv:
            raise forms.ValidationError("Please upload your CV")
        
        # Validate file size (5MB limit)
        max_size = 5 * 1024 * 1024  # 5MB
        if cv.size > max_size:
            raise forms.ValidationError(
                f"File too large. Maximum size is {max_size//(1024*1024)}MB"
            )
        
        # Validate file extension
        valid_extensions = ['pdf', 'doc', 'docx']
        ext = cv.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise forms.ValidationError(
                "Unsupported file format. Please upload a PDF or Word document"
            )
        
        return cv



from django import forms
from .models import JobApplication

class JobApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']
