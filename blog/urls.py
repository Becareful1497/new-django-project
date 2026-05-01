from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message, name='message'),
    path('emodji/', views.emodji, name='emodji'),
    path('blog_list/', views.blog_list_view, name='blog_list'),
    path('blog_list/<int:id>/', views.blog_detail_view, name='blog_id'),
    
]