from django import forms

class ImportTestForm(forms.Form):
    excel_file = forms.FileField(label='Select Excel File')