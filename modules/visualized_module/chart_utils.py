
color_dict = {
    "uptrend":"limegreen",
    "sideway":"skyblue",
    "downtrend":"firebrick"
}

def define_color(value):
    list_colors = [color_dict["uptrend"]]
    for i in range(len(value))[1:]:
        if value[i] > value[i-1]:
            list_colors.append(color_dict["uptrend"])
        elif value[i] == value[i-1]:
            list_colors.append(color_dict["sideway"])
        else:
            list_colors.append(color_dict["downtrend"])
    return list_colors