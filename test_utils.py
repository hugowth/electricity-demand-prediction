from unittest import TestCase
from utils import convert_date, get_date_range


class ConvertDateTestCase(TestCase):
    def test_convert_date(self):
        result = convert_date("01/01/2022 00")

        self.assertEqual(result, "2022-01-01 00:00:00.000000")

    def test_convert_date_fail(self):
        result = convert_date("01/01/2022 00*")

        self.assertEqual(result, None)


class GetDateRangeTestCase(TestCase):
    def test_get_date_range(self):
        date_range = get_date_range()

        self.assertEqual(len(date_range), 20)
        self.assertEqual(date_range[0]["start"], "01012022")
        self.assertEqual(date_range[0]["end"], "01312022")
        self.assertEqual(date_range[19]["start"], "08012023")
        self.assertEqual(date_range[19]["end"], "08312023")
