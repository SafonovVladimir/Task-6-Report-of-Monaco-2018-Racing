import datetime


def convert_to_milliseconds(time):
    return (time.hour * 60 + time.minute * 60 + time.second) * 1000 + time.microsecond // 1000


def get_lap_time(t1, t2):
    """Return string with time lap"""

    delta = convert_to_milliseconds(t2) - convert_to_milliseconds(t1)
    lap_time = datetime.datetime.fromtimestamp(delta / 1000)
    return "%s:%s.%0.3d" % (lap_time.minute, lap_time.second, lap_time.microsecond // 1000)
