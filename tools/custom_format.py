from tools import utils

def format_sequential_data(source:list,nums_of_digit=5):
    # Get data
    list_time_step = [data[0] for data in source]
    list_value = [data[1] for data in source]

    # Normalize data
    # Convert time to understandable format
    list_time_step = [utils.seconds_to_datetime(time_data) for time_data in list_time_step]
    # Limit digit after comma
    list_value = [round(value,nums_of_digit) for value in list_value]

    return list_time_step,list_value