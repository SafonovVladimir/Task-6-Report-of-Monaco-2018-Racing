from pathlib import Path

ABBREIVIATIONS = Path(__file__).parent.parent / 'data/abbreviations.txt'


def get_time(text):
    return text.split("_")[1].split("\n")[0]


def get_abb(text):
    return text.split("_")[0]


def get_abb_from_name(name):
    for k, v in make_driver_name_dict(ABBREIVIATIONS).items():
        if v == name:
            return str(k)


def get_driver_name(text):
    return text.split("_")[1]


def get_team_name(text):
    return text.split("_")[2].split("\n")[0]


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


def make_driver_time(abb, time):
    start_time = {}
    for i in read_file(time):
        if abb in get_abb_list(ABBREIVIATIONS):
            start_time[i[:3]] = get_time(i)
    return start_time


def make_driver_time_dict(abb, time):
    start_time = {}
    for i in read_file(time):
        if i[:3] in get_abb_list(abb):
            start_time[i[:3]] = get_time(i)
    return start_time


def make_driver_name_dict(abb):
    name_dict = {}
    for i in read_file(abb):
        if i[:3] in get_abb_list(abb):
            name_dict[i[:3]] = get_driver_name(i)
    return name_dict
