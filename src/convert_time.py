import datetime


def convert_to_milliseconds(time):
    return (time.hour * 60 + time.minute * 60 + time.second) * 1000 + time.microsecond // 1000


def convert_to_time(time):
    """Return string with time lap"""
    time = datetime.datetime.fromtimestamp(time / 1000.0)
    return "%s:%s.%0.3d" % (time.minute, time.second, time.microsecond // 1000)
