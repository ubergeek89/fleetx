from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
import pytz
from django.utils import timezone

class SuperAdminMiddleware(MiddlewareMixin):
	def process_request(self, request):
		if request.user.is_superuser:
			if request.path.startswith('/admin/')==False:
				return HttpResponseRedirect("/admin")
		return None

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                timezone.activate(pytz.timezone(str(request.user.contact.account.timezone)))