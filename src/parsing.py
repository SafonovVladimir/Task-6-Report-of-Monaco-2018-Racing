from datetime import datetime
from pathlib import WindowsPath


def read_file(file):
    try:
        with open(file, 'r') as f:
            return f.readlines()
    except OSError:
        raise OSError(f'{file} does not exist.')


def get_time(text):
    return text.split("_")[1].split("\n")[0]


def get_abb(text):
    return text.split("_")[0]


def get_abb_from_name(path, name):
    return ''.join(k for k, v in make_driver_name_dict(WindowsPath(path)).items() if v == name)


def get_driver_name(text):
    return text.split("_")[1]


def get_team_name(text):
    return text.split("_")[2].split("\n")[0]


def get_team_from_name(path, name):
    return ''.join(v for k, v in make_driver_team_dict(WindowsPath(path)).items() if k == name)


def get_team_list(path):
    return [get_team_name(i) for i in read_file(path)]


def get_abb_list(abbreviations):
    return [get_abb(i) for i in read_file(abbreviations)]


def make_driver_time_dict(abb, time):
    return {i[:3]: get_time(i) for i in read_file(time) if i[:3] in get_abb_list(abb)}


def make_driver_name_dict(path):
    return {get_abb(i): get_driver_name(i) for i in read_file(path) if get_abb(i) in get_abb_list(path)}


def make_driver_team_dict(path):
    return {get_driver_name(i): get_team_name(i) for i in read_file(path) if get_abb(i) in get_abb_list(path)}


def get_driver_time(path, time, key):
    return datetime.strptime(make_driver_time_dict(path, time).get(key), '%H:%M:%S.%f').time()
