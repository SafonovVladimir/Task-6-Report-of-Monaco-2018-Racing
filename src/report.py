import click
from prettytable import PrettyTable
from make_report import build_report


def print_report(path, name, rev):
    count = 1
    table = PrettyTable()
    table.field_names = ["Number", "Driver name", "Team name", "Lap time"]
    for key, value in build_report(path, name, rev).items():
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
@click.option('--file', nargs=1, help='Enter the PATH to Folder with data files')
@click.option('--driver', nargs=1, default=None, help='Enter the drivers name to show data')
@click.option('--desc', is_flag=True, help='Show revers result')
def cli(file, desc, driver):
    if driver:
        print_report(file, driver, desc)
    else:
        if desc:
            print_report(file, driver, desc)
        else:
            print_report(file, driver, desc)


if __name__ == '__main__':
    cli()
