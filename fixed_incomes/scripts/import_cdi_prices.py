import csv, os
import logging
from datetime import datetime
from django.db import transaction
from fixed_incomes.models import CdiPrice


@transaction.atomic
def run():
    import_cdi_prices()


def import_cdi_prices():
    current_folder = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_path = os.path.join(current_folder, "CDI_Prices.csv")

    insert_list = []

    with open(file_path, 'r', newline='') as csv_file:
        for row in csv.DictReader(csv_file):
            date = datetime.strptime(row['dtDate'], '%d/%m/%Y')
            insert_list.append(CdiPrice(date=date, trade_price=row['dLastTradePrice']))

        CdiPrice.objects.bulk_create(insert_list, ignore_conflicts=True)
        logging.info('Data imported.')


