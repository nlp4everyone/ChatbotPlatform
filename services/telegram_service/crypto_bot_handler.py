from telethon import events
import asyncio
from services.telegram_service.base import base_markup
from modules.api_module.exchange_api import CoingeckoAPI,PeriodType
from modules.visualized_module.chart import CustomChart
from modules import utils,algorithm
failed_data_message = "Cannot get data from Coingecko"

@events.register(events.NewMessage(pattern="/start"))
async def start_chat_handler(event):
    # Important parameter
    chat = await event.get_chat() # Get chat object

    # Define client
    client = event.client
    # Send message back
    async with client.action(chat, 'typing') as action:
        await asyncio.sleep(1)
        await client.send_message(chat,'Hello')

@events.register(events.NewMessage(pattern="/price"))
async def price_chart_handler(event):
    # Important parameter
    chat = await event.get_chat() # Get chat object


    # Define client
    client = event.client
    # Send message back
    async with client.action(chat, 'typing') as action:
        # Get information about market history
        market_history = CoingeckoAPI.get_market_history(days=2,period_type=PeriodType.HOURLY)
        #
        if market_history is not None:
            # Select only price value
            list_price = market_history['prices']
            # print value
            price_time, price_formatted_value, price_color, price_text = utils.format_index(list_price,n_digits=3)

            # Error value
            error_value = algorithm.get_value(price_formatted_value)
            # Waterfall value
            bottom, height = algorithm.get_waterfall_value(error_value,price_formatted_value)
            # Index
            index = [i for i in range(len(price_time))]
            # Display waterfall chart
            CustomChart.display_waterfall(index,height,bottom,price_formatted_value,price_color)
            await client.send_file(entity=chat, file="price_chart.png", force_document=False, clear_draft=True)

@events.register(events.NewMessage(pattern="/marketcap"))
async def marketcap_chart_handler(event):
    # Important parameter
    chat = await event.get_chat() # Get chat object

    # Define client
    client = event.client
    # Send message back
    async with client.action(chat, 'typing') as action:
        # Get information about market history
        market_history = CoingeckoAPI.get_market_history()

        # Empty data case
        if market_history == None:
            await client.send_message(chat, failed_data_message)
        else:
            # Select only price value
            marketcaps_stats = market_history['market_caps']
            # Get formatted date
            marketcaps_time, marketcaps_formatted_value, marketcaps_color,marketcaps_text = utils.format_index(marketcaps_stats,sort=True)
            # Display chart
            CustomChart.display_barh(indexs=marketcaps_time,values=marketcaps_formatted_value,labels_name=marketcaps_text,color=marketcaps_color)

            # Send chart
            caption = f"Okay, sure. Current market cap is {marketcaps_text[-1]}"
            # await client.send_file(entity=chat, file=chart,force_document=False)
            await client.send_file(entity=chat, file="market_chart.png",force_document=False,clear_draft=True,caption=caption)

@events.register(events.CallbackQuery())
async def callback_query_handler(event):
    print("Callback query handler")
    # Callback query handler
    print(dir(event))

    # Button click
    data = event.data

    # Get message
    message = await event.get_message()
    sender = await event.get_sender()

    # Define client
    client = event.client