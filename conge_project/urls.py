"""
URL configuration for conge_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from employes import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path('redirect_after_login/', views.redirect_after_login, name='redirect_after_login'),
    path("conge/", views.mes_conges, name="mes_conges"),
    path("demande/", views.demander_conge, name="demander_conge"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("dash/", views.admin_conges, name="admin_conges"),
]
