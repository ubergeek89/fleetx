from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'fleetxapp'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('emailconfirm/<slug:uid>/', views.EmailConfirmView.as_view(), name='emailconfirm'),
    path('forgotpassword/', views.ForgotPasswordView.as_view(), name='forgotpassword'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('fileupload/', views.FileUploadView.as_view(), name='fileupload'),
    path('newcomment/<slug:object_type>/<int:object_id>/', views.CommentAddView.as_view(), name='commentadd'),

    path('vehicles/', views.VehicleListView.as_view(), name='vehicles'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicledetail'),
    path('vehicle/<int:pk>/edit', views.VehicleEditView.as_view(), name='vehicleedit'),    
    path('vehicle/add', views.VehicleAddView.as_view(), name='vehicleadd'),    
    path('vehicle/<int:pk>/photos', views.VehiclePhotosView.as_view(), name='vehiclephotos'),
    path('vehicle/<int:pk>/documents', views.VehicleDocumentsView.as_view(), name='vehiclesdocuments'),
    path('vehicle/<int:pk>/comments', views.VehicleCommentsView.as_view(), name='vehiclecomments'),
    path('vehicle/<int:pk>/reminders', views.VehicleAllRemindersView.as_view(), name='vehicleallreminders'),
    path('vehicle/<int:pk>/issues', views.VehicleAllIssues.as_view(), name='vehicleallissues'),
    path('vehicle/<int:pk>/fuelentries', views.VehicleAllFuelEnties.as_view(), name='vehicleallfuelentries'),    

    path('vehiclereminders/', views.VehicleReminderListView.as_view(), name='vehiclereminders'),
    path('vehiclereminders/<int:pk>/new', views.VehicleReminderAddView.as_view(), name='vehicleremindersadd'),
    path('vehiclereminders/edit/<int:pk>/', views.VehicleReminderEditView.as_view(), name='vehicleremindersedit'),    

    path('servicereminders/', views.ServiceReminderListView.as_view(), name='servicereminders'),
    path('servicereminders/<int:pk>/new', views.ServiceReminderAddView.as_view(), name='serviceremindersadd'),
    path('servicereminders/edit/<int:pk>/', views.ServiceReminderEditView.as_view(), name='serviceremindersedit'),

    path('issues/', views.IssuesListView.as_view(), name='issues'),
    path('issues/<int:pk>/new', views.IssueAddView.as_view(), name='issuesadd'),
    path('issues/edit/<int:pk>/', views.IssueEditView.as_view(), name='issuesedit'),

    path('vendors/', views.VendorsListView.as_view(), name='vendors'),
    path('vendors/new', views.VendorsAddView.as_view(), name='vendorsadd'),
    path('vendors/edit/<int:pk>/', views.VendorsEditView.as_view(), name='vendorsedit'),

    path('fuelentries/', views.FuelEntryListView.as_view(), name='fuelentries'),
    path('fuelentries/<int:pk>/new', views.FuelEntryAddView.as_view(), name='fuelentriesadd'),
    path('fuelentries/edit/<int:pk>/', views.FuelEntryEditView.as_view(), name='fuelentriesedit'),

    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('settings/', views.SettingsView.as_view(), name='settings'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]