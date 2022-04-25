"""appointment_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from office_app.views import Home, AppointmentView, PhysicianCreateView, PhysicianListView, PhysicianEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('appointments/', AppointmentView.as_view(), name='appointments'),

    path('add_physician/', PhysicianCreateView.as_view(), name='add_physician'),
    path('list_physician/', PhysicianListView.as_view(), name='list_physician'),
    path('edit_physician/<slug:first_name>/<slug:last_name>/<slug:speciality>', PhysicianEditView.as_view(), name='edit_physician'),
]
