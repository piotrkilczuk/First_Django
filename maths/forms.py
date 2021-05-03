from django.forms import ModelForm
from .models import Result, Math

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ["value", "error"]
        
        def clean(self):
            cleaned_data = super().clean()
            value = cleaned_data.get('value')
            error = cleaned_data.get('error')

            if value and error:
                raise forms.ValidationError("Podaj tylko jedną z wartości")
            elif not (value or error):
                raise forms.ValidationError("Nie podano żadnej wartości!")

class MathForm(ModelForm):
    class Meta:
        model = Math
        fields = ['a', 'b', 'operation', 'result']
