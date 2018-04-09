from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models

class RegisterForm(forms.Form):
	organization_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Organization Name'}))
	fleet_size = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Number Of Vehicles'}))	
	full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full Name'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'E-Mail Address'}))
	phone_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}))
	password = forms.CharField(max_length=30, min_length=8, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))
	confirm_password = forms.CharField(max_length=30, min_length=8, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError("Passwords Do Not Match")

		email = cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("User with this email address already exists")

class ForgotPasswordForm(forms.Form):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'E-Mail Address'}))

	def clean(self):
		cleaned_data = super(ForgotPasswordForm, self).clean()
		email = cleaned_data.get("email")
		if not User.objects.filter(email=email).exists():
			raise forms.ValidationError("User with this email address does not exist")

class LoginForm(forms.Form):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'E-Mail Address'}))
	password = forms.CharField(max_length=30, min_length=8, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		email = cleaned_data.get("email")
		if not User.objects.filter(email=email).exists():
			raise forms.ValidationError("User with this email address does not exist")

class VehicleForm(forms.ModelForm):
	class Meta:
		model=models.Vehicle
		exclude = ['account']
		widgets = {
			'vehicle_type': forms.Select(attrs={'class':'select2'}),
			'profilepicture': forms.Select(attrs={'class':'select2'}),
			'status': forms.Select(attrs={'class':'select2'}),
			'make': forms.Select(attrs={'class':'select2'}),
			'model': forms.Select(attrs={'class':'select2'}),
			'assigned_to': forms.Select(attrs={'class':'select2'}),
		}

class VehicleRenewalReminderForm(forms.ModelForm):
	class Meta:
		model=models.VehicleRenewalReminder
		exclude = ['account']
		widgets = {
			'vehicle': forms.Select(attrs={'class':'select2'}),
			'vehicle_reminder_type': forms.Select(attrs={'class':'select2'}),
			'notify_contacts': forms.SelectMultiple(attrs={'class':'select2', 'multiple':'multiple'}),
		}

class ServiceReminderForm(forms.ModelForm):
	class Meta:
		model=models.ServiceReminders
		exclude = ['account']
		widgets = {
			'vehicle': forms.Select(attrs={'class':'select2'}),
			'service_reminder_type': forms.Select(attrs={'class':'select2'}),
			'notify_contacts': forms.SelectMultiple(attrs={'class':'select2', 'multiple':'multiple'}),
		}

class IssueForm(forms.ModelForm):
	class Meta:
		model=models.Issues
		exclude = ['account']
		widgets = {
			'vehicle': forms.Select(attrs={'class':'select2'}),
			'current_status': forms.Select(attrs={'class':'select2'}),			
			'reported_by': forms.Select(attrs={'class':'select2'}),				
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model=models.Comments
		exclude = ['account','author','timestamp','linked_object_type','linked_object_id']

class VendorsForm(forms.ModelForm):
	class Meta:
		model=models.Vendors
		exclude = ['account']
		widgets = {
			'vendor_type': forms.Select(attrs={'class':'select2'}),
		}

class FuelEntryForm(forms.ModelForm):
	class Meta:
		model=models.FuelEntry
		exclude = ['account']
		widgets = {
			'vehicle': forms.Select(attrs={'class':'select2'}),
			'vendor': forms.Select(attrs={'class':'select2'}),			
		}

class ServiceEntryForm(forms.ModelForm):
	class Meta:
		model=models.ServiceEntry
		exclude = ['account']
		widgets = {
			'vehicle': forms.Select(attrs={'class':'select2'}),
			'vendor': forms.Select(attrs={'class':'select2'}),			
		}

class ContactForm(forms.ModelForm):
	class Meta:
		model=models.Contact
		exclude = ['account','user','is_owner']
		widgets = {
			'profilepicture': forms.Select(attrs={'class':'select2'}),
		}
