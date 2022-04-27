# from pathlib import Path
from unittest import TestCase, main
from datetime import datetime

from src.parsing import get_team_list
from tests import get_abb_from_name#, make_driver_time
from tests import convert_to_milliseconds, get_lap_time, print_report, build_report
from tests import get_abb_list, get_time, make_driver_time_dict, get_abb, make_driver_name_dict

ABBREIVIATIONS = 'D:\PythonProjects\Task 6 Report of Monaco 2018 Racing/tests/test_data'
END = 'D:\PythonProjects\Task 6 Report of Monaco 2018 Racing/tests/test_data/end.log'
START = 'D:\PythonProjects\Task 6 Report of Monaco 2018 Racing/tests/test_data/start.log'
NAME = 'Daniel Ricciardo'
FMT = '%H:%M:%S.%f'


class TestCollection(TestCase):
    """Test"""

    def test_get_abb(self):
        """Test get_abb"""
        self.assertEqual(get_abb('DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'), 'DRR')

    def test_get_abb_list(self):
        """Test abbreviations"""
        self.assertEqual(get_abb_list(ABBREIVIATIONS + '\\abbreviations.txt'), ['DRR'])

    def test_get_team_list(self):
        """Test abbreviations"""
        self.assertEqual(get_team_list(ABBREIVIATIONS + '\\abbreviations.txt'), ['RED BULL RACING TAG HEUER'])

    def test_get_abb_from_name(self):
        """Test abbreviations"""
        self.assertEqual(get_abb_from_name(ABBREIVIATIONS, NAME), 'DRR')

    def test_get_time(self):
        """Test get_time"""
        self.assertEqual(get_time('DRR2018-05-24_12:14:12.054'), '12:14:12.054')

    def test_make_driver_time_dict(self):
        """Test get_driver_time"""
        self.assertEqual(make_driver_time_dict(ABBREIVIATIONS + '\\abbreviations.txt', START), {'DRR': '12:14:12.054'})

    # def test_make_driver_time(self):
    #     """Test get_driver_time"""
    #     self.assertEqual(make_driver_time('DRR', START), {'DRR': '12:14:12.054'})

    def test_make_driver_name_dict(self):
        """Test get_driver_time"""
        self.assertEqual(make_driver_name_dict(ABBREIVIATIONS + '\\abbreviations.txt'), {'DRR': 'Daniel Ricciardo'})

    def test_convert_to_milliseconds(self):
        """Test convert_to_milliseconds"""
        self.assertEqual(convert_to_milliseconds(datetime.strptime('1:13.393', "%M:%S.%f")), 73393)

    def test_get_lap_time(self):
        """Test get_lap_time"""
        t1 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS + '\\abbreviations.txt', START).get('DRR'),
                               FMT).time()
        t2 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS + '\\abbreviations.txt', END).get('DRR'),
                               FMT).time()
        self.assertEqual(get_lap_time(t1, t2), '1:12.013')

    def test_build_report(self):
        """Test build_report"""
        self.assertEqual(build_report(ABBREIVIATIONS, NAME),
                         {'DRR': ('Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '1:12.013')})

    def test_print_report_name(self):
        """Test print_report"""
        self.assertEqual(print_report(ABBREIVIATIONS, NAME), None)

    def test_print_report_without_name(self):
        """Test print_report"""
        self.assertEqual(print_report(ABBREIVIATIONS, None), None)


if __name__ == '__main__':
    main()
