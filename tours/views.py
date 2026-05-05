from django.views.generic import ListView
from .models import TourCompany

class TourCompanyListView(ListView):
    model = TourCompany
    template_name = 'tours/company_list.html'
    context_object_name = 'companies'
