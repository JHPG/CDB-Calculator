from django.http import JsonResponse
from django.shortcuts import render


def calculate_cdb(request):
    return JsonResponse({
        's': 2
    })


