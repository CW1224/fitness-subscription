from django import forms
from .models import Review

RATINGS = [(1, 'Very bad'),
           (2, 'Bad'),
           (3, 'Ok'),
           (4, 'Good'),
           (5, 'Great!')]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(label='How will you rate this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)