import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

class CustomChart():
    @staticmethod
    def display_waterfall(index=None,height=None,bottom=None,value=None,color=None):
        # Show value
        plt.bar(x=index, height=height, bottom=bottom,label="Price",color=color)
        # Min display
        lower_threshold = min(value) * 0.99
        upper_threshold = max(value) * 1.01

        # Limit
        plt.ylim([lower_threshold,upper_threshold])

        # Add config
        plt.title("Price in last 3 days")
        plt.xlabel("Date")
        plt.ylabel("Price(USD)")
        plt.savefig('price_chart.png')

    @staticmethod
    def display_barh(indexs=None,values=None,labels_name=None,color=None):
        # # Display chart
        # plt.bar(x=labels,height=width,color=color,label="market value")
        # # Display trend
        # plt.plot(width,linestyle = 'dashed',marker = 'o',label="trending")
        #
        # # Add config
        # plt.title("Market caps in last 7 days")
        # plt.xlabel("Date")
        # plt.ylabel("Value in millions")
        # plt.legend()

        # Display chart
        fig, ax = plt.subplots()
        ax.barh(y=indexs,width=values,color=color,label="Market value")

        # Display text
        for i, v in enumerate(values):
            ax.text(v, i, str(v),color='black')

        # Add config
        plt.title("Market caps in last 7 days",color="darkorange")
        plt.xlabel("Value in millions")
        plt.ylabel("Date")
        plt.legend(loc='upper right')

        plt.savefig('market_chart.png')



