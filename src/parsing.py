def get_time(text):
    return text.split("_")[1].split("\n")[0]

def get_abb(text):
    return text.split("_")[0]

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


def get_driver_time(abb, time):
    start_time = {}
    for i in read_file(time):
        if i[:3] in get_abb_list(abb):
            start_time[i[:3]] = get_time(i)
    return start_time
