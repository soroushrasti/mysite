from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
]