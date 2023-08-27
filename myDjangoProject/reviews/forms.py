from django import forms

from .models import Review
"Server as from behavior in django"


# class ReviewForm(forms.Form):
#     " Review form value and behavior"
#     user_name = forms.CharField(label="Your Name", required=True, max_length=100, error_messages={
#         "required": "Your Name must not empty!",
#         "max_lenngth": "Please pick shorter name than 100 char"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    " Creating form based of models"
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['user_name', 'review_text', 'rating']
        # exlcude = ['rating']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_message = {
            "user_name": {
                "required": "Your Name must not empty!",
                "max_lenngth": "Please pick shorter name than 100 char"
            }
        }
