from pathlib import Path
from parsing import read_file, make_driver_time_dict, get_abb, get_driver_name, get_team_name, get_abb_from_name
from datetime import datetime
from convert_time import get_lap_time

ABBREIVIATIONS = Path(__file__).parent.parent / 'data/abbreviations.txt'
END = Path(__file__).parent.parent / 'data/end.log'
START = Path(__file__).parent.parent / 'data/start.log'
FMT = '%H:%M:%S.%f'


def build_report(text):
    lap_time = {}
    all_data_dict = {}
    if type(text) == str:
        for i in read_file(ABBREIVIATIONS):
            if text == get_driver_name(i):
                key = get_abb_from_name(text)
                driver_name = text
                team_name = get_team_name(i)
                t1 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, START).get(key), FMT).time()
                t2 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, END).get(key), FMT).time()
                lap_time[key] = get_lap_time(t1, t2)
                all_data_dict[key] = driver_name, team_name, lap_time[key]
            else:
                continue
    else:
        for i in read_file(text):
            key = get_abb(i)
            driver_name = get_driver_name(i)
            team_name = get_team_name(i)
            t1 = datetime.strptime(make_driver_time_dict(text, START).get(key), FMT).time()
            t2 = datetime.strptime(make_driver_time_dict(text, END).get(key), FMT).time()
            lap_time[key] = get_lap_time(t1, t2)
            all_data_dict[key] = driver_name, team_name, lap_time[key]
    return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))

# def build_report_by_driver_name(name):
#     lap_time = {}
#     all_data_dict = {}
#     for i in read_file(ABBREIVIATIONS):
#         if name == get_driver_name(i):
#             key = get_abb_from_name(name)
#             driver_name = name
#             team_name = get_team_name(i)
#             t1 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, START).get(key), FMT).time()
#             t2 = datetime.strptime(make_driver_time_dict(ABBREIVIATIONS, END).get(key), FMT).time()
#             lap_time[key] = get_lap_time(t1, t2)
#             all_data_dict[key] = driver_name, team_name, lap_time[key]
#     return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
