from django import forms
from django.contrib.auth.models import User


"""
Constants
"""
ERROR_MESSAGE_USER = {'required': 'El username es requerido','unique': 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto'} 
ERROR_MESSAGE_PASSWORD = {'required': 'El password es requerido'}
ERROR_MESSAGE_EMAIL = {'required': 'El email es requerido','invalid': 'Ingrese un correo valido'}


"""
Function
"""

def muts_be_gt(value_password):
	if len(value_password) < 5:
		raise forms.ValidationError('El password debe contener al menos 5 caracteres, desde una func')

"""
Class 
"""
class LoginUserForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput())

class CreateUserForm(forms.ModelForm):
	username = forms.CharField(max_length = 20, error_messages = ERROR_MESSAGE_USER )
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput(), error_messages = ERROR_MESSAGE_PASSWORD )
	email = forms.CharField(error_messages = ERROR_MESSAGE_EMAIL)

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class EditUserForm(forms.ModelForm):
	username = forms.CharField(max_length = 20, error_messages = ERROR_MESSAGE_USER )
	email = forms.CharField(error_messages = ERROR_MESSAGE_EMAIL)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

class EditPasswordForm(forms.Form):
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput())
	new_password = forms.CharField(max_length = 20, widget = forms.PasswordInput(), validators = [muts_be_gt])
	repeat_password = forms.CharField(max_length = 20, widget = forms.PasswordInput(), validators = [muts_be_gt])

	def clean(self):
		clean_data = super(EditPasswordForm,self).clean()
		password1 = clean_data.get('new_password')
		password2 = clean_data.get('repeat_password')

		if password1 != password2:
			raise forms.ValidationError('Los password no son los mismos')