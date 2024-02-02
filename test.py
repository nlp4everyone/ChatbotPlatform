from format import custom_format
from service.exchange_api import CoingeckoAPI
market_data = CoingeckoAPI.get_market_history()
price_time_data = market_data['prices']
# list_time_step,list_value = custom_format.format_sequential_data(price_time_data, nums_of_digit=5)
# samples = [0.73856, 0.75555, 0.8397, 0.82835, 0.80679, 0.86653, 0.87201, 0.84907, 0.84059, 0.83247, 0.82539, 0.72459, 0.72536, 0.78077, 0.80206, 0.77207, 0.76475, 0.73992, 0.72906, 0.72614, 0.83312, 0.82314, 0.76636, 0.77, 0.79173, 0.79932, 0.77424, 0.81587, 0.81537, 0.77499, 0.72559, 0.76214, 0.75594, 0.71148, 0.75338, 0.75962, 0.76909, 0.77413, 0.74078, 0.70838, 0.69446, 0.69173, 0.68955, 0.74459, 0.74727, 0.70982, 0.70315, 0.62111, 0.6473]
from waterfall_ax import WaterfallChart
import matplotlib.pyplot as plt
# print(list_time_step[-10:-1])
# print(list_value[-10:-1])

#
# Plot
# waterfall = WaterfallChart(list_value)
# wf_ax = waterfall.plot_waterfall(title='A Simple Example')
# plt.show()
# print(np.array([1,2,3,4]-np.array([5,5,5,5])))
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