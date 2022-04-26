from parsing import read_file, get_driver_time
from datetime import datetime
from convert_time import convert_to_milliseconds, convert_to_time

ABBREIVIATIONS = 'abbreviations.txt'
END = 'end.log'
START = 'start.log'
FMT = '%H:%M:%S.%f'

def build_report(file):
    lap_time = {}
    all_data_dict = {}
    for i in read_file(file):
        key = i.split("_")[0]
        driver_name = i.split("_")[1]
        team_name = i.split("_")[2].split("\n")[0]
        abb = i.split("_")[0]
        t1 = datetime.strptime(get_driver_time(ABBREIVIATIONS, START).get(abb), FMT).time()
        t2 = datetime.strptime(get_driver_time(ABBREIVIATIONS, END).get(abb), FMT).time()
        delta = convert_to_time(convert_to_milliseconds(t2) - convert_to_milliseconds(t1))
        lap_time[abb] = delta
        if key not in all_data_dict:
            all_data_dict[key] = driver_name, team_name, lap_time[abb]
    return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))