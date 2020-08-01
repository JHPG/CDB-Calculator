import json
from datetime import datetime, timedelta
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render

from fixed_incomes.models import CdiPrice


def calculate_cdb(request):
    """ Calculates the accumulated daily CDI rate, given a JSON with start and end date """
    cdb_data = json.loads(request.body)

    # Get the values and convert the dates
    investment_date = datetime.strptime(cdb_data['investmentDate'], '%Y-%m-%d')
    current_date = datetime.strptime(cdb_data['currentDate'], '%Y-%m-%d') - timedelta(days=1)
    cdb_rate = Decimal(cdb_data['cdbRate'])

    # Fetch the CDI rates from db between the dates
    prices_list = CdiPrice.objects.filter(date__range=(investment_date, current_date)).values('trade_price', 'date')

    unit_prices = []
    accumulated_rate = 1

    for cdi_data in prices_list:
        daily_rate = cdi_data['trade_price']
        # For each item, calculate the CDI rate with a round of 8 decimal places
        tcdi = round(((daily_rate/100 + 1) ** Decimal(1/252))-1, 8)
        # Join the result with a round of 16 decimal places to the accumulated rate
        accumulated_rate = round(accumulated_rate * (1 + tcdi * cdb_rate / 100), 16)
        # Append the new value to final list
        unit_prices.append({
            "date": cdi_data['date'].strftime('%Y-%m-%d'),
            "unitPrice": accumulated_rate,
        })

    return JsonResponse(unit_prices, safe=False)


