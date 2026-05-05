from django.urls import path
from .views import TourCompanyListView

urlpatterns = [
    path('', TourCompanyListView.as_view(), name='tour_company_list'),
]
