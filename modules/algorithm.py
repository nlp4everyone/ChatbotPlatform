def sort_value(time_list,value_list):

    # Find index with duplicated
    # unique_time = sorted(list(set(time_list)),reverse=True)
    unique_time = []
    for element in time_list:
        if element not in unique_time:
            unique_time.append(element)

    duplicate_keys = [item for item in unique_time if time_list.count(item) > 1]

    output_time = []
    output_value = []
    for i in range(len(unique_time)):
        # Not duplicate element
        if unique_time[i] not in duplicate_keys:
            index = time_list.index(unique_time[i])
            output_time.append(time_list[index])
            output_value.append(value_list[index])
        else:
            # Get list
            list_index = [y for (y,element) in enumerate(time_list) if element == unique_time[i]]
            # Choose max index
            max_index = max(list_index)
            output_time.append(time_list[max_index])
            output_value.append(value_list[max_index])

    return output_time,output_value

def get_value(value_list,n_digits=3):
    output = [value_list[0]]
    for i in range(len(value_list))[1:]:
        error = round(value_list[i]-value_list[i-1],n_digits)
        output.append(error)
    return output

def get_waterfall_value(error_value:list,cum_value:list):
    bottom = [0]
    height = [cum_value[0]]

    for i, val in enumerate(error_value[1:], start=1):
        if val == 0:  ## Current Value equal to 0
            bottom.append(cum_value[i])
            height.append(0.01)
        elif val > 0:  ## Current Value greater than 0
            if error_value[i - 1] >= 0:
                bottom.append(cum_value[i - 1])
            else:
                bottom.append(bottom[i - 1])
            height.append(val)
        elif val < 0:  ## Current Value less than 0
            if error_value[i - 1] >= 0:
                bottom.append(cum_value[i - 1] + val)
            else:
                bottom.append(bottom[i - 1] + val)
            height.append(-val)

    return bottom,height