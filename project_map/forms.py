from django import forms

from project_map.models import Rayon, Category, Rubric


class RegionForm(forms.Form):
    reg_choices = forms.ModelChoiceField(queryset=Rayon.objects.all(), label='', empty_label="Выберите муниципальное образование", widget=forms.Select(attrs={'class': 'form-control rayon-select',}))


WHO_CHOICES=[('Взрослые','Взрослые'),
         ('Дети','Дети'),
         ('С животными','С животными'),]


def transit_choices():
    CATEGORY_CHOICES = []
    for item in Category.objects.all():
        CATEGORY_CHOICES.append((item.title, item.title))

    return CATEGORY_CHOICES

def to_choices():
    rubric_list = Rubric.objects.filter(parent__id = 1)
    TO_CHOICES = [(item.slug, item.title) for item in rubric_list]

    return TO_CHOICES

def category_choices():
    rubric_list = Rubric.objects.filter(parent__slug = "classification")
    TO_CHOICES = [(item.slug, item.title) for item in rubric_list]

    return TO_CHOICES

class FromTravelingForm(forms.Form):
    from_t = forms.CharField(label = 'От куда едем?', max_length = 500, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    who_t = forms.MultipleChoiceField(label="Кто едет?", choices=WHO_CHOICES, widget=forms.CheckboxSelectMultiple(
        attrs={"class": "list-unstyled"}), required=True)

    categories = forms.MultipleChoiceField(label="Что Вам интересно?", choices=category_choices,
                                   widget=forms.CheckboxSelectMultiple(attrs={"class": "list-unstyled"}), required=True)

    transit = forms.MultipleChoiceField(label="Дополнительные объекты", choices=transit_choices,
                                   widget=forms.CheckboxSelectMultiple(attrs={"class": "list-unstyled"}), required=True)


class ToTravelingForm(forms.Form):
    answer = forms.MultipleChoiceField(label="", choices=to_choices, widget=forms.CheckboxSelectMultiple(attrs={"class": "list-unstyled"}), required=True)