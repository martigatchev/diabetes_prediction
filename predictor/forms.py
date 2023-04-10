from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0, 'max': 20, 'value': 0}),
        label="Pregnancies"
    )
    glucose = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0, 'max': 200, 'value': 0}),
        label="Glucose"
    )
    bmi = forms.FloatField(
        widget=forms.NumberInput(attrs={'min': 15, 'max': 70, 'value': 15}),
        label="BMI"
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 18, 'max': 80, 'value': 18}),
        label="Age"
    )
