from django import forms

from catalog.models import Product, Version


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def search_word(self, enter):
        for word in self.danger_words:
            if word in enter.lower():
                raise forms.ValidationError(f'Вах, дорогой, не надо так. Давай без "{word}"')


class ProductForm(StyleForMixin, forms.ModelForm):
    danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'overview', 'category', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        self.search_word(cleaned_data)
        return cleaned_data

    def clean_overview(self):
        cleaned_data = self.cleaned_data.get('overview')
        self.search_word(cleaned_data)
        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
