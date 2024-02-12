import datetime
import math

def convert_second_to_date(seconds):
    # Convert milisecond to second
    seconds /= 1000
    # Convert to time
    time = datetime.datetime.fromtimestamp(seconds)
    # Formatted time
    formatted_time = f"{time.day}/{time.month}"
    return formatted_time

def millify(n,n_digits=1):
    n = float(n)
    millnames = ['','K','M','B','T']
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    # Get value
    value = round(n / 10**(3 * millidx),n_digits)
    # Return value
    full_value = f"{value}{millnames[millidx]}"
    raw_value = value
    return full_value,raw_value
