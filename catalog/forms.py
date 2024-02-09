from django import forms

from catalog.models import Product, Version


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FindBadWord:

    def search_word(self, enter):
        for word in self.danger_words:
            if word in enter.lower():
                raise forms.ValidationError(f'Вах, дорогой, не надо так. Давай без "{word}"')


class ProductForm(StyleForMixin, FindBadWord, forms.ModelForm):
    danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'overview', 'category', 'price', 'is_active')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        self.search_word(cleaned_data)
        return cleaned_data

    def clean_overview(self):
        cleaned_data = self.cleaned_data.get('overview')
        self.search_word(cleaned_data)
        return cleaned_data


class VersionForm(StyleForMixin, FindBadWord, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def clean_sign(self):
    #     cleaned_data = self.cleaned_data.get('sign')
    #     # return cleaned_data
    #
    #     if cleaned_data and self.instance.product.version_set.filter(sign=True).exclude(
    #             id=self.instance.id).exists():
    #         raise forms.ValidationError('Может существовать только одна активная версия!')
    #
    #     return cleaned_data

    # def clean_sign(self):
    #     cleaned_data = self.cleaned_data.get('sign')
    #     num_true = Version.objects.all().filter(product_id=self.get_object().id)
    #     numm = 0
    #     for i in num_true:
    #         if i.sign:
    #             numm += 1
    #     if numm > 1:
    #         raise forms.ValidationError(f'Увы, не больше одного варианта в наличии')
