# from datetime import datetime
from pathlib import WindowsPath


# from src.convert_time import get_lap_time


def get_time(text):
    return text.split("_")[1].split("\n")[0]


def get_abb(text):
    return text.split("_")[0]


def get_abb_from_name(path, name):
    for k, v in make_driver_name_dict(WindowsPath(path + '\\abbreviations.txt')).items():
        if v == name:
            return str(k)


def get_driver_name(text):
    return text.split("_")[1]


def get_team_name(text):
    return text.split("_")[2].split("\n")[0]


def get_team_from_name(path, name):
    for k, v in make_driver_team_dict(WindowsPath(path + '\\abbreviations.txt')).items():
        if k == name:
            return str(v)


def get_team_list(path):
    team_list = []
    for i in read_file(path):
        team_list.append(get_team_name(i))
    return team_list


def get_abb_list(abbreviations):
    abb_list = []
    for i in read_file(abbreviations):
        abb_list.append(get_abb(i))
    return abb_list


def read_file(file):
    try:
        with open(file, 'r') as f:
            return f.readlines()
    except OSError:
        raise OSError(f'{file} does not exist.')


# def make_driver_time(abb, time):
#     start_time = {}
#     for i in read_file(time):
#         if abb in get_abb_list(WindowsPath(abb + '\\abbreviations.txt')):
#             start_time[i[:3]] = get_time(i)
#     return start_time


def make_driver_time_dict(abb, time):
    start_time = {}
    for i in read_file(time):
        if i[:3] in get_abb_list(abb):
            start_time[i[:3]] = get_time(i)
    return start_time


def make_driver_name_dict(path):
    name_dict = {}
    for i in read_file(path):
        if get_abb(i) in get_abb_list(path):
            name_dict[get_abb(i)] = get_driver_name(i)
    return name_dict


def make_driver_team_dict(path):
    team_dict = {}
    for i in read_file(path):
        if get_abb(i) in get_abb_list(path):
            team_dict[get_driver_name(i)] = get_team_name(i)
    return team_dict
