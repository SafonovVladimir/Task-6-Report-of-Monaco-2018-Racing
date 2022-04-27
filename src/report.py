from pathlib import Path
from src.parsing import read_file, get_driver_time
from datetime import datetime
from src.convert_time import get_lap_time

ABBREIVIATIONS = Path(__file__).parent.parent / 'data/abbreviations.txt'
END = Path(__file__).parent.parent / 'data/end.log'
START = Path(__file__).parent.parent / 'data/start.log'
FMT = '%H:%M:%S.%f'


def build_report(file):
    lap_time = {}
    all_data_dict = {}
    for i in read_file(file):
        key = i.split("_")[0]
        driver_name = i.split("_")[1]
        team_name = i.split("_")[2].split("\n")[0]
        abb = i.split("_")[0]
        t1 = datetime.strptime(get_driver_time(file, START).get(abb), FMT).time()
        t2 = datetime.strptime(get_driver_time(file, END).get(abb), FMT).time()
        lap_time[abb] = get_lap_time(t1, t2)
        all_data_dict[key] = driver_name, team_name, lap_time[abb]
    return dict(sorted(all_data_dict.items(), key=lambda item: item[1][2]))
