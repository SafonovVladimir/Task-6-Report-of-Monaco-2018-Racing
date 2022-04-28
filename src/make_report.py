from src.parsing import *
from src.convert_time import get_lap_time

all_data_dict = {}


def build_report(path, name, rev):
    start = WindowsPath(path + '/start.log')
    end = WindowsPath(path + '/end.log')
    add_path = WindowsPath(path + '/abbreviations.txt')
    for k, v in make_driver_name_dict(add_path).items():
        if name == v:
            key = get_abb_from_name(add_path, name)
            team_name = get_team_from_name(add_path, name)
            get_dict(add_path, start, end, key, name, team_name)
            return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
    else:
        for i in read_file(add_path):
            key = get_abb(i)
            driver_name = get_driver_name(i)
            team_name = get_team_name(i)
            get_dict(add_path, start, end, key, driver_name, team_name)
        return dict(sorted(all_data_dict.items(), reverse=rev, key=lambda item: item[1][2]))


def get_dict(path, start, end, key, name, team):
    time_start = get_driver_time(path, start, key)
    time_end = get_driver_time(path, end, key)
    all_data_dict[key] = name, team, get_lap_time(time_start, time_end)
