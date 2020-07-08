from django import forms

class GeneralForm(forms.Form):
    institute = forms.CharField()
class SponseredForm(GeneralForm):
   pass
class CollaborativeForm(GeneralForm):
   pass
class ConsultancyForm(GeneralForm):
   pass