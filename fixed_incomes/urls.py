from django.urls import path

from fixed_incomes import views

urlpatterns = [

    path('cdb/calculate', views.api_calculate_cdb, name='calculate_cdb'),

]

