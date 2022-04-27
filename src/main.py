from pathlib import WindowsPath
import click
from prettytable import PrettyTable
from report import build_report#, ABBREIVIATIONS, START, END


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


@click.command(context_settings={"ignore_unknown_options": True})
@click.option('--file', nargs=1, help='Enter the PATH to data files')
@click.option('--driver', nargs=1, help='Enter the PATH to data files')
def make_cli(file, driver):
    if driver:
        print_report(driver)
    else:
        print_report(file)


if __name__ == '__main__':
    print_report('D:\data')
    # print_report('Daniel Ricciardo')
    # print_report('Romain Grosjean')
    # make_cli()
