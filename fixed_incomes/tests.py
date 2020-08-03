from decimal import Decimal

from django.test import TestCase

from fixed_incomes.managers.cdb_manager import calculate_cdb
from fixed_incomes.scripts.import_cdi_prices import import_cdi_prices


class TestCdb(TestCase):

    def setUp(self):
        # Use import script function to populate database with CSV
        import_cdi_prices()

    def test_cdb_calculation(self):
        cdb_data = {
            "investmentDate": "2016-11-14",
            "cdbRate": 103.5,
            "currentDate": "2016-12-26"
        }
        unit_prices = calculate_cdb(cdb_data)
        places = 13     # decimal places to assert in test
        self.assertAlmostEqual(unit_prices[0]['unitPrice'], Decimal(1.0005339668500000), places=places)
        self.assertAlmostEqual(unit_prices[-1]['unitPrice'], Decimal(1.0154454495839100), places=places)


