from django import forms
from .models import Interview, ReviewQuestion, InterviewReview
from jobs.models import JobApplication

from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the job_application field from the form since we're setting it in the view
        if 'job_application' in self.fields:
            del self.fields['job_application']

    class Meta:
        model = Interview
        fields = ['scheduled_time', 'interview_link']  # Only include existing fields
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ReviewQuestionForm(forms.ModelForm):
    class Meta:
        model = ReviewQuestion
        fields = ['question_text']

class InterviewReviewForm(forms.ModelForm):
    class Meta:
        model = InterviewReview
        fields = ['question', 'rating',]
