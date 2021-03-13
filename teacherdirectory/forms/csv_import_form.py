from django import forms

class CSVImportForm(forms.Form):
    file = forms.FileField()