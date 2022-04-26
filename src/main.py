ABBREIVIATIONS = 'abbreviations.txt'
END = 'end.log'
START = 'start.log'


def read_file(file):
    try:
        with open(file, 'r') as f:
            return f.readlines()
            # for line in f.readlines():
            #     print(f.readline())
            # f.close()
    except OSError:
        raise OSError(f'{file} does not exist.')


def get_abb(abbreviations):
    abb = []
    for i in read_file(abbreviations):
        abb.append(i.split("_")[0])
    return abb


def get_team_name(abbreviations):
    team_name = []
    for i in read_file(abbreviations):
        team_name.append(i.split("_")[2].split("\n")[0])
    return team_name


def get_time(file):
    time = []
    for i in read_file(file):
        time.append(i.split("_")[1].split("\n")[0])
    return time


print(get_time(END))
# print(get_abb(ABBREIVIATIONS))
# print(get_team_name(ABBREIVIATIONS))
# print(read_file(ABBREIVIATIONS))
# get_time(ABBREIVIATIONS, START)
# get_time(ABBREIVIATIONS, END)
# print(read_file(START))
