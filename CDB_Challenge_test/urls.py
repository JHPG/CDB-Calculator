""" Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('', lambda r: HttpResponse('<h1>Hello!</h1>')),

    # Import urls from 'fixed-incomes' url file
    path('fixed-incomes/', include('fixed_incomes.urls')),

]

