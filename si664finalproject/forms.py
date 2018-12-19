from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from si664finalproject.models import Hospital


class si664finalprojectForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ['provider_identifier','hospital_name', 'address', 'phone_number']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))
