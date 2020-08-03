import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

from fixed_incomes.managers.cdb_manager import calculate_cdb


def api_calculate_cdb(request):
    """ Calculates the accumulated daily CDI rate, given a JSON with start and end date """
    # Get the data either by JSON (request body) or querystring
    cdb_data = json.loads(request.body) if request.body else request.GET

    # Check if it have the right parameters
    if 'investmentDate' in cdb_data and 'currentDate' in cdb_data and 'cdbRate' in cdb_data:
        unit_prices = calculate_cdb(cdb_data)
        return JsonResponse(unit_prices, safe=False)
    else:
        return HttpResponseBadRequest('Bad parameters :(')


def page_cdb_calc(request):
    return render(request, 'fixed_incomes/cdb_calculation.html')


