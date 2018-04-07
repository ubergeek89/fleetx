from django.contrib import admin
from . import models

admin.site.site_title = 'FleetX Administration'
admin.site.site_header = 'FleetX Administration'

@admin.register(models.Signups)
class SignupsAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'organization_name', 'full_name', 'email', 'password')

@admin.register(models.Account)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'owner', 'timezone', 'accountstatus', 'signup_timestamp')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'full_name')

@admin.register(models.MasterVehicleTypes)
class MasterVehicleTypesAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle_type')

@admin.register(models.MasterVehicleStatus)
class MasterVehicleStatusAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle_status', 'color')

@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'registration_number', 'vehicle_type', 'status')

@admin.register(models.MasterMakes)
class MasterMakesAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle_make')

@admin.register(models.MasterModels)
class MasterModelsAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle_make', 'vehicle_model')

@admin.register(models.MasterVehicleReminderTypes)
class MasterVehicleReminderTypesAdmin(admin.ModelAdmin):
    list_display = ('account', 'reminder_type')

@admin.register(models.VehicleReminders)
class VehicleRemindersAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle', 'vehicle_reminder_type')

@admin.register(models.MasterServiceReminderTypes)
class MasterServiceReminderTypesAdmin(admin.ModelAdmin):
    list_display = ('account', 'reminder_type')

@admin.register(models.ServiceReminders)
class ServiceRemindersAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle', 'service_reminder_type')

@admin.register(models.Issues)
class IssuesAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle', 'current_status')

@admin.register(models.MasterVendorTypes)
class MasterVendorTypesAdmin(admin.ModelAdmin):
    list_display = ('account', 'vendor_type')

@admin.register(models.Vendors)
class VendorsAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'vendor_type')

@admin.register(models.FuelEntry)
class FuelEntryAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle', 'date','quantity')

@admin.register(models.ServiceEntry)
class ServiceEntryAdmin(admin.ModelAdmin):
    list_display = ('account', 'vehicle', 'date','vendor')













@admin.register(models.Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('account', 'file_type', 'linked_object_type')

@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('account', 'author', 'timestamp','linked_object_type')
