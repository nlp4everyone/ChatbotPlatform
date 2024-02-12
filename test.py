
keys = ["5/6","6/6","6/6","7/6","8/6","8/6","8/6"]
values = [1200,1301,1201,1044,6565,2332,1202]

print()
def sort_value(time_list,value_list):

    # Find index with duplicated
    unique_time = sorted(list(set(time_list)))
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
