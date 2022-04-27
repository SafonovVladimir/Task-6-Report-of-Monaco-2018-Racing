from parsing import *
from datetime import datetime
from convert_time import get_lap_time


def build_report(path, name, rev):
    lap_time = {}
    all_data_dict = {}
    start = WindowsPath(path + '/start.log')
    end = WindowsPath(path + '/end.log')
    add_path = WindowsPath(path + '/abbreviations.txt')
    driver_name_dict = make_driver_name_dict(add_path)
    for k, v in driver_name_dict.items():
        if name == v:
            key = get_abb_from_name(add_path, name)
            driver_name = name
            team_name = get_team_from_name(add_path, name)
            t1 = datetime.strptime(make_driver_time_dict(add_path, start).get(key), FMT).time()
            t2 = datetime.strptime(make_driver_time_dict(add_path, end).get(key), FMT).time()
            lap_time[key] = get_lap_time(t1, t2)
            all_data_dict[key] = driver_name, team_name, lap_time[key]
            return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
    else:
        for i in read_file(add_path):
            key = get_abb(i)
            driver_name = get_driver_name(i)
            team_name = get_team_name(i)
            t1 = datetime.strptime(make_driver_time_dict(add_path, start).get(key), FMT).time()
            t2 = datetime.strptime(make_driver_time_dict(add_path, end).get(key), FMT).time()
            lap_time[key] = get_lap_time(t1, t2)
            all_data_dict[key] = driver_name, team_name, lap_time[key]
        return dict(sorted(all_data_dict.items(), reverse=rev, key=lambda item: item[1][2]))
