from waterfall_ax import WaterfallChart
import matplotlib.pyplot as plt
import numpy as np

class CustomChart():
    @staticmethod
    def show_candle_chart(index,height,bottom):
        # Show value
        plt.bar(x=index, height=height, bottom=bottom)
        plt.show()

def show_chart():
    # The height
    height = [6, 2, 1]
    bottom = [0, 6 , 7]
    index = np.arange(len(height))
    print(index)

    # Show value
    plt.bar(x=index,height=height,bottom=bottom)
    plt.show()

