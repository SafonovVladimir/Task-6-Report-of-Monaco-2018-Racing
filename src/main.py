from prettytable import PrettyTable
from src.report import build_report, ABBREIVIATIONS


def print_report(file):
    count = 1
    table = PrettyTable()
    table.field_names = ["Number", "Driver name", "Team name", "Lap time"]
    for key, value in build_report(file).items():
        if count < 16:
            table.add_row([count, value[0], value[1], value[2]])
            count += 1
        elif count == 16:
            table.add_row(["-" * 6, "-" * 17, "-" * 25, "-" * 8])
            table.add_row([count, value[0], value[1], value[2]])
            count += 1
        else:
            table.add_row([count, value[0], value[1], value[2]])
            count += 1
    print(table)

if __name__ == '__main__':
    print_report(ABBREIVIATIONS)
