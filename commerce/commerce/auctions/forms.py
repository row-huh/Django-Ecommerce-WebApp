from django.forms import ModelForm, ChoiceField
from .models import Listing

class ListingForm(ModelForm):
    categories = ChoiceField(choices=[
    ('option1', 'Display Option 1'),
    ('option2', 'Display Option 2'),
    ], required=False)
    class Meta:
        model = Listing
        fields = ['title', 'description', 'categories', 'imageURL']