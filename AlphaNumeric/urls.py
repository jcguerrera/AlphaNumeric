"""AlphaNumeric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Interpolation import views as Interpolation_views
from nonlinearEquations import views as NoLinearEquations
from AlphaNumeric import views as AlphaNumeric_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lagrangeP/', Interpolation_views.lagrangeP, name='inter_lagrangeP'),
    path('biseccion/', NoLinearEquations.bisectionP, name='no_lineal_biseccion'),
    path('busquedas/',NoLinearEquations.incremental_SearchP, name ='no_lineal_Search'),
    path('index/', AlphaNumeric_views.index, name='alpha_views'),
]
