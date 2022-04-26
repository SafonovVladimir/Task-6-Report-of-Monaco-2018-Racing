from report import build_report, ABBREIVIATIONS


def print_report(file):
    count = 1
    for key, value in build_report(file).items():
        if count < 16:
            print(f'{count}. {value[0]}   |  {value[1]}    |  {value[2]}')
            count += 1
        else:
            print('-' * 150)
            print(f'{count}. {value[0]}')
            count += 1


# print(get_abb(ABBREIVIATIONS))
# t1 = datetime.strptime(get_driver_time(ABBREIVIATIONS, START).get('LHM'), FMT).time()
# t2 = datetime.strptime(get_driver_time(ABBREIVIATIONS, END).get('LHM'), FMT).time()
# delta = convert_to_time(convert_to_milliseconds(t2) - convert_to_milliseconds(t1))
# print(delta)
# print(convert_to_time(convert_to_milliseconds(t1)))
# print(convert_to_time(delta))
print_report(ABBREIVIATIONS)
# print(make_driver_time(ABBREIVIATIONS))
# print(make_dict(ABBREIVIATIONS))


# print(get_driver_time(ABBREIVIATIONS, START).get('VBM'))
# print(get_driver_time(ABBREIVIATIONS, END).get('VBM'))
# add_start_time(START)
# print(get_driver_time(ABBREIVIATIONS, END))
# print(all_data_dict)
# print(get_driver_lap_time(ABBREIVIATIONS, START, END))
# print(get_abb(ABBREIVIATIONS))
# get_time(ABBREIVIATIONS, END)
# print(read_file(START))
