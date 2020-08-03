""" Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.shortcuts import redirect
from django.urls import path, include, reverse

from fixed_incomes.views import page_cdb_calc

urlpatterns = [
    path('', lambda r: redirect(reverse('page_cdb_calc'))),

    # Import urls from 'fixed-incomes' url file
    path('api/fixed-incomes/', include('fixed_incomes.urls')),
    path('tools/cdb', page_cdb_calc, name='page_cdb_calc'),

]

