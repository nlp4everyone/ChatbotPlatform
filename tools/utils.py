import datetime
from enum import Enum
class TimeFormat(Enum):
    HOUR_MINUTE_SECOND = 0
    HOUR_MINUTE = 1

def seconds_to_datetime(seconds:int,format = TimeFormat.HOUR_MINUTE):
    # Convert miliseconds to seconds
    seconds /= 1000
    # Convert time
    formatted_time = datetime.datetime.fromtimestamp(seconds)
    # Get hour, minute and second
    hour = formatted_time.hour
    minute = formatted_time.minute
    second = formatted_time.second

    # Get output
    output = ""
    if format == TimeFormat.HOUR_MINUTE:
        output = f"{hour}:{minute}"
    elif format == TimeFormat.HOUR_MINUTE_SECOND:
        output = f"{hour}:{minute}:{second}"
    return output
