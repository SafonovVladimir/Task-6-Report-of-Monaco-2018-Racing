from pathlib import Path
from unittest import TestCase, main
from datetime import datetime
from tests import convert_to_milliseconds, get_lap_time
from tests import print_report
from tests import get_abb_list, get_time, get_driver_time, get_abb
from tests import build_report

ABBREIVIATIONS = Path(__file__).parent.parent / 'tests/test_data/abbreviations.txt'
END = Path(__file__).parent.parent / 'tests/test_data/end.log'
START = Path(__file__).parent.parent / 'tests/test_data/start.log'
FMT = '%H:%M:%S.%f'


class TestCollection(TestCase):
    """Test"""

    def test_get_abb(self):
        """Test get_abb"""
        self.assertEqual(get_abb('DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'), 'DRR')

    def test_get_abb_list(self):
        """Test abbreviations"""
        self.assertEqual(get_abb_list(ABBREIVIATIONS), ['DRR'])

    def test_get_time(self):
        """Test get_time"""
        self.assertEqual(get_time('DRR2018-05-24_12:14:12.054'), '12:14:12.054')

    def test_get_driver_time(self):
        """Test get_driver_time"""
        self.assertEqual(get_driver_time(ABBREIVIATIONS, START), {'DRR': '12:14:12.054'})

    def test_convert_to_milliseconds(self):
        """Test convert_to_milliseconds"""
        self.assertEqual(convert_to_milliseconds(datetime.strptime('1:13.393', "%M:%S.%f")), 73393)

    def test_get_lap_time(self):
        """Test get_lap_time"""
        t1 = datetime.strptime(get_driver_time(ABBREIVIATIONS, START).get('DRR'), FMT).time()
        t2 = datetime.strptime(get_driver_time(ABBREIVIATIONS, END).get('DRR'), FMT).time()
        self.assertEqual(get_lap_time(t1, t2), '1:12.013')

    def test_build_report(self):
        """Test build_report"""
        self.assertEqual(build_report(ABBREIVIATIONS),
                         {'DRR': ('Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '1:12.013')})

    def test_print_report(self):
        """Test print_report"""
        self.assertEqual(print_report(ABBREIVIATIONS), None)


if __name__ == '__main__':
    main()
