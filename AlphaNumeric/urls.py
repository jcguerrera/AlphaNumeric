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
from GaussianElimination import views as GaussianElimination_views
from LUFactorization import views as LU_Factorization
from Iterative import views as Sor
from Interpolation import views as Diferencies

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AlphaNumeric_views.index, name='alpha_views'),
    path('lagrangeP/', Interpolation_views.lagrangeP, name='inter_lagrangeP'),
    path('vandermonde/', Interpolation_views.vandermondeP, name='inter_vandermonde'),
    path('biseccion/', NoLinearEquations.bisectionP, name='no_lineal_biseccion'),
    path('busquedas/',NoLinearEquations.incremental_SearchP, name ='no_lineal_Search'),
    path('reglafalsa/',NoLinearEquations.falseRuleP, name ='no_lineal_reglafalsa'),
    path('gaussian_elimination/',GaussianElimination_views.GaussianEliminationP, name ='gaussianElimination'),
    path('LU_Factorization/',LU_Factorization._simpleLU, name ='LU_Factorization'),
    path('sor/',Sor._sor, name ='sor'),
    path('divide_diferencies/',Diferencies._NewtonP, name ='divide_diferencies'),
    path('index/', AlphaNumeric_views.index, name='alpha_views'),
]
