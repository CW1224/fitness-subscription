from django import forms
from .models import Review

RATINGS = [(1, 'Very Bad'),
           (2, 'Not great'),
           (3, 'Not too bad'),
           (4, 'Good'),
           (5, 'Amazing')]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(label='How will you rate your experience with this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
