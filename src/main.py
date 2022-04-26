from report import build_report, ABBREIVIATIONS


def print_report(file):
    count = 1
    for key, value in build_report(file).items():
        if count <= 15:
            print(f'{count}. {value[0]}   |  {value[1]}    |  {value[2]}')
            count += 1
        else:
            # print('-' * 150)
            print(f'{count}. {value[0]}   |  {value[1]}    |  {value[2]}')
            count += 1


print_report(ABBREIVIATIONS)
