from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Signups(models.Model):
	uuid = models.CharField(max_length=100)
	organization_name = models.CharField(max_length=100)
	full_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.uuid + " - " + self.email

class Account(models.Model):
	ACCOUNT_STATUS = (
			('FREETRIAL', 'FREETRIAL'),
			('PAID', 'PAID')
		)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	organization_name = models.CharField(max_length=100)
	timezone = models.CharField(max_length=100, default="GMT")
	accountstatus = models.CharField(max_length=50, choices=ACCOUNT_STATUS, default="FREETRIAL")
	signup_timestamp = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return "Account ID: "+ str(self.pk) + " Owner: "+ self.owner.username




class Files(models.Model):
	FILE_TYPES = (
			('IMAGE', 'IMAGE'),
			('DOCUMENT', 'DOCUMENT'),
		)
	OBJECT_TYPE = (
			('Vehicle', 'Vehicle'),
			('VehicleRenewalReminder', 'VehicleRenewalReminder'),
			('ServiceReminders', 'ServiceReminders'),
			('Issues','Issues'),
			('FuelEntry','FuelEntry'),
			('ServiceEntry','ServiceEntry'),
			('Contact','Contact'),
		)

	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	uuid = models.CharField(max_length=500)
	url = models.CharField(max_length=500)
	file_type = models.CharField(max_length=20, choices=FILE_TYPES)
	linked_object_type = models.CharField(max_length=20, choices=OBJECT_TYPE)
	linked_object_id = models.IntegerField()
	upload_timestamp = models.DateTimeField(default = datetime.now)
	uploaded_by = models.ForeignKey("Contact", on_delete=models.DO_NOTHING)

	def __str__(self):
		return "File: "+ str(self.name)



class Contact(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	profilepicture = models.ForeignKey(Files, on_delete=models.DO_NOTHING, blank=True, null=True)
	full_name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	is_driver = models.BooleanField(default=False)
	is_owner = models.BooleanField(default=False)
	is_user = models.BooleanField(default=False)

	def __str__(self):
		return "Contact: "+ str(self.full_name)


class MasterVehicleTypes(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle_type = models.CharField(max_length=30)

	def __str__(self):
		return "VehicleType: "+ str(self.vehicle_type)

class MasterVehicleStatus(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle_status = models.CharField(max_length=30)
	color = models.CharField(max_length=30, blank=False)

	def __str__(self):
		return "VehicleStatus: "+ str(self.vehicle_status)

class MasterMakes(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle_make = models.CharField(max_length=30)

	def __str__(self):
		return "VehicleMakes: "+ str(self.vehicle_make)

class MasterModels(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle_make = models.ForeignKey(MasterMakes, on_delete=models.CASCADE)
	vehicle_model = models.CharField(max_length=30)

	def __str__(self):
		return "VehicleModel: "+ str(self.vehicle_model)

class Vehicle(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	profilepicture = models.ForeignKey(Files, on_delete=models.DO_NOTHING, blank=True, null=True)
	name = models.CharField(max_length=30)
	registration_number = models.CharField(max_length=30)
	vehicle_type = models.ForeignKey(MasterVehicleTypes, on_delete=models.CASCADE)
	status = models.ForeignKey(MasterVehicleStatus, on_delete=models.CASCADE)
	year = models.IntegerField()
	make = models.ForeignKey(MasterMakes, on_delete=models.CASCADE, blank=True, null=True)
	model = models.ForeignKey(MasterModels, on_delete=models.CASCADE, blank=True, null=True)
	assigned_to = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return "Vehicle: "+ str(self.name)


class MasterVehicleRenewalReminderType(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	reminder_type = models.CharField(max_length=70)

	def __str__(self):
		return "MasterVehicleRenewalReminderType: "+ str(self.reminder_type)

class VehicleRenewalReminder(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	vehicle_reminder_type = models.ForeignKey(MasterVehicleRenewalReminderType, on_delete=models.CASCADE)
	due_date = models.DateField()
	days_treshold = models.IntegerField()
	email_notifications = models.BooleanField()
	notify_contacts = models.ManyToManyField(Contact, related_name="reminders", blank=True)

	def __str__(self):
		return "VehicleRenewalReminder: "+ str(self.id)

class MasterServiceReminderTypes(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	reminder_type = models.CharField(max_length=70)

	def __str__(self):
		return "VehicleReminderType: "+ str(self.reminder_type)

class ServiceReminders(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	service_reminder_type = models.ForeignKey(MasterServiceReminderTypes, on_delete=models.CASCADE)
	odometer_reading = models.IntegerField()
	odometer_treshold = models.IntegerField()
	email_notifications = models.BooleanField()
	notify_contacts = models.ManyToManyField(Contact, related_name="servicereminders", blank=True)

	def __str__(self):
		return "ServiceReminders: "+ str(self.id)


class Issues(models.Model):
	STATUS_CHOICES = (
			('OPEN','OPEN'),
			('WORKING', 'WORKING'),
			('CLOSED','CLOSED')
		)
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	reported_date = models.DateField()
	reported_by = models.ForeignKey(Contact, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	description = models.TextField(max_length=10000, blank=True,null=True)
	current_status = models.CharField(max_length=200, choices=STATUS_CHOICES)
	due_date = models.DateField()

	def __str__(self):
		return "Issue: "+ str(self.id)


class MasterVendorTypes(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vendor_type = models.CharField(max_length=100)

	def __str__(self):
		return "VendorType: "+ self.vendor_type


class Vendors(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	vendor_type = models.ForeignKey(MasterVendorTypes, on_delete=models.DO_NOTHING)

	def __str__(self):
		return "Vendor: "+ self.name


class FuelEntry(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	date = models.DateField()
	price = models.DecimalField(max_digits=10, default=0, decimal_places=5, blank=True)
	quantity = models.DecimalField(max_digits=10, default=0, decimal_places=5, blank=True)
	total_amount = models.DecimalField(max_digits=10, default=0, decimal_places=5, blank=True)
	vendor = models.ForeignKey(Vendors, on_delete=models.DO_NOTHING, blank=True, null=True)

	def __str__(self):
		return "FuelEntry: "+ str(self.id)


class ServiceEntry(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	date = models.DateField()
	total_amount = models.DecimalField(max_digits=10, default=0, decimal_places=5, blank=True)
	vendor = models.ForeignKey(Vendors, on_delete=models.DO_NOTHING, blank=True, null=True)

	def __str__(self):
		return "ServiceEntry: "+ str(self.id)








class Comments(models.Model):
	OBJECT_TYPE = (
			('Vehicle', 'Vehicle'),
			('VehicleRenewalReminder', 'VehicleRenewalReminder'),
			('ServiceReminders', 'ServiceReminders'),
			('Issues','Issues'),
			('FuelEntry','FuelEntry'),
			('ServiceEntry','ServiceEntry'),
			('Contact','Contact'),
		)

	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	author = models.ForeignKey(Contact, on_delete=models.CASCADE)
	timestamp= models.DateTimeField(default=datetime.now)
	comment_text = models.TextField(max_length=10000)
	linked_object_type = models.CharField(max_length=20, choices=OBJECT_TYPE)
	linked_object_id = models.IntegerField()

	def __str__(self):
		return "Comment: "+ str(self.pk)