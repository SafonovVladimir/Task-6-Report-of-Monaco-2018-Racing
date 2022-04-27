from pathlib import Path, WindowsPath
from parsing import *
from datetime import datetime
from convert_time import get_lap_time

ABBREIVIATIONS = Path(__file__).parent.parent / 'data/abbreviations.txt'
END = Path(__file__).parent.parent / 'data/end.log'
START = Path(__file__).parent.parent / 'data/start.log'
FMT = '%H:%M:%S.%f'


def build_report(text):
    lap_time = {}
    all_data_dict = {}
    for i in read_file(ABBREIVIATIONS):
        driver_name_dict = make_driver_name_dict(ABBREIVIATIONS)
        for k, v in driver_name_dict.items():
            if text == v:
                key = get_abb_from_name(text)
                driver_name = text
                team_name = get_team_name(i)
                t1 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, START).get(key), FMT).time()
                t2 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, END).get(key), FMT).time()
                lap_time[key] = get_lap_time(t1, t2)
                all_data_dict[key] = driver_name, team_name, lap_time[key]
                return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
        else:
            start = WindowsPath(text + '\start.log')
            end = WindowsPath(text + '\end.log')
            abbreiviations = WindowsPath(text + '\\abbreviations.txt')
            for i in read_file(abbreiviations):
                key = get_abb(i)
                driver_name = get_driver_name(i)
                team_name = get_team_name(i)
                t1 = datetime.strptime(make_driver_time_dict(abbreiviations, start).get(key), FMT).time()
                t2 = datetime.strptime(make_driver_time_dict(abbreiviations, end).get(key), FMT).time()
                lap_time[key] = get_lap_time(t1, t2)
                all_data_dict[key] = driver_name, team_name, lap_time[key]
        return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
