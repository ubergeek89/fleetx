from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView, View, ListView, FormView
from django.http import Http404
from FleetXApp import utils

class IndexView(View):
	def get(self, request):
		return render(request, "website/index.html")
	def post(self, request, *args, **kwargs):
		name = request.POST.get('name','')
		phone = request.POST.get('phone','')
		fleet_size = request.POST.get('fleet_size','')
		template = get_template('emails/newlead.html')
		html_content = template.render({"name":name, "phone":phone, "fleet_size":fleet_size, "thank_you":True})
		subject = "New Lead At FleetX"

		utils.send_email(subject,"aditya@espertosys.com",html_content)
		return render(request, "website/index.html")