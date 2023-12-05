from django import forms
from django.contrib.auth.models import User

from .models import Books

genre_choices = (
    ("Programmer", "Programmer"),
    ("App Developer", "App Developer"),
    ("Python", "Python"),
    ("Web Designer", "Web Designer"),
    ("FullStack", "FullStack"),
    ("Vedio Edit", "Vedio Edit"),
    ("Professional", "Professional"),
    ("Others", "Others"),

)


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Job title",
                            help_text="How your job will be called")
    genre = forms.CharField(max_length=255, label="Who make this", help_text="Choose who should do the work",
                            widget=forms.Select(choices=genre_choices))
    price = forms.DecimalField(max_digits=55, decimal_places=2, label="Price",
                               help_text="Please enter price")
    image = forms.ImageField(required=False, label="Layout image",
                             help_text="Please submit your website design")
    description = forms.CharField(max_length=300, label="Description", help_text="Please enter description",
                                  widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))

    class Meta:
        model = Books
        fields = ['title', 'genre', 'price', 'image', 'description']