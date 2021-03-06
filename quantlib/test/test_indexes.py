"""
 Copyright (C) 2011, Enthought Inc
 Copyright (C) 2011, Patrick Henaff

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

import unittest

from quantlib.currency import USDCurrency
from quantlib.index import Index
from quantlib.indexes.interest_rate_index import InterestRateIndex
from quantlib.indexes.libor import Libor
from quantlib.settings import Settings
from quantlib.time.api import Days, ModifiedFollowing, Months, Period, TARGET
from quantlib.time.api import Actual360, today

class TestIndex(unittest.TestCase):

    def test_create_index(self):

        with self.assertRaises(ValueError):
            Index()

class TestIRIndex(unittest.TestCase):

    def test_create_index(self):

        with self.assertRaises(ValueError):
            InterestRateIndex()

class TestLibor(unittest.TestCase):

    def test_create_libor_index(self):

        settings = Settings.instance()

        # Market information
        calendar = TARGET()

        # must be a business day
        eval_date = calendar.adjust(today())
        settings.evaluation_date = eval_date


        settlement_days = 2
        settlement_date = calendar.advance(eval_date, settlement_days, Days)
        # must be a business day
        settlement_date = calendar.adjust(settlement_date);

        end_of_month = True

        index = Libor('USD Libor', Period(6, Months), settlement_days,
                        USDCurrency(), calendar, ModifiedFollowing,
                        end_of_month, Actual360())

        self.assertEquals('USD Libor6M Actual/360', index.name)

if __name__ == '__main__':
    unittest.main()
