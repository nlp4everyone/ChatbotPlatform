from modules.visualized_module import chart_utils
from modules.api_module import api_utils
from modules import algorithm
def format_index(stats,sort=False,n_digits=1):
    # Parse value
    stat_time = [api_utils.convert_second_to_date(stat[0]) for stat in stats]
    stat_value = [stat[1] for stat in stats]

    # Remove duplicate value( Get last)
    if sort: stat_time,stat_value = algorithm.sort_value(stat_time,stat_value)

    # Normalize
    formatted_value = [api_utils.millify(stat,n_digits=n_digits)[1] for stat in stat_value]
    text_value = [api_utils.millify(stat)[0] for stat in stat_value]
    # Define color
    stat_color = chart_utils.define_color(stat_value)
    return stat_time,formatted_value,stat_color,text_value


