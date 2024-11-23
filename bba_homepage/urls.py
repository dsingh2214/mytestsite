from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_homepage, name='home'),
    path('about-us', views.render_about_us, name='about-us'),
    path('contact-us', views.render_contact_us, name='contact-us'),
    path('services', views.render_services, name='services'),
    path('under-construction', views.render_under_construction, name='under-construction'),
]
