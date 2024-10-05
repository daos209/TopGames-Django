"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
<<<<<<<<< Temporary merge branch 1

urlpatterns = [
    path('admin/', admin.site.urls),
]
=========
from django.urls import path
from .views import UserLoginAPIView, PayPalExecuteAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginAPIView.as_view(), name='api_login'),
    path('paypal/execute/', PayPalExecuteAPIView.as_view(), name='api_paypal_execute'),
]

>>>>>>>>> Temporary merge branch 2
