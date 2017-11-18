from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout

from beers.models import Company, Beer


# Form
# class CompanyForm(forms.Form):
#     name = forms.CharField(required=True)
#     tax_num = forms.IntegerField(required=True, label="Tax number", initial=0)


# ModelForm
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'tax_number']
        # help_texts = {'name': "How is it gonna be called?"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'company-form'
        self.helper.form_class = 'blue'
        # self.helper.label_class = 'col-lg-3'
        # self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout('tax_number', 'name')
        # self.helper.layout.append(
        #         HTML("""<button>A</button>"""),
        #     )

        self.helper.add_input(Submit('submit-name', 'Guardar'))

    def clean_name(self):
        data = self.cleaned_data['name']

        if data == "florida":
            raise ValidationError("That name is forbidden.", code="invalid-name")

        return data

    def clean(self):
        cleaned_data = super().clean() # ensures that any validation logic in parent classes is maintained

        name = self.cleaned_data.get("name")
        tax = self.cleaned_data.get("tax_number")

        if name == "michigan" and tax > 100:
            error_msg = "No aceptamos ese nombre para un numero tan alto"
            # self.add_error('name', error_msg)  # field error
            raise ValidationError(error_msg)  # form error

        return cleaned_data


class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        exclude = ['created_at', 'created_by', 'last_modified_at', 'last_modified_by']


BeerFormset = inlineformset_factory(Company, Beer, form=BeerForm, extra=2)