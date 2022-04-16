import math

hours = 0
minutes = 0
seconds = 0
num = 0

def get_hour(epoch_seconds):
    if (epoch_seconds < 3600):
        return 0
    else:
        hours = math.trunc(epoch_seconds / 3600)
        return hours

def get_minutes(epoch_seconds):
    if ((epoch_seconds % 3600) == 0):
        return 0
    else:
        minutes = epoch_seconds % 3600
        minutes = math.trunc(minutes / 60)
        return minutes

def get_seconds(epoch_seconds):
    if ((epoch_seconds % 3600) == 0):
        return 0
    else:
        seconds = epoch_seconds % 3600
        if (seconds >= 60):
            while seconds >= 60:
                seconds -= 60
        return seconds

def time_from_utc(utc_offset, utc_zero):
    return (utc_offset + utc_zero)

def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes  = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridiem

    return  time