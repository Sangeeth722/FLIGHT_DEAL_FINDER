#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
import flight_data
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv


load_dotenv("C:/Users/sangeeth/PycharmProjects/EnvironmentVariables/.env.txt") #To find env variable from mmy local

BOT_TOKEN = os.getenv("bot_token_telegram") #Telegram Bot token
BOT_CHATID = os.getenv("bot_chatId_telegram")#Telegram ChatID


SHEETY_ENDPONT =os.getenv("SHEETY_ENDPOINT")
KIVI_API =os.getenv("KIVI_API")


SEARCH_ENDPOINT =os.getenv("SEARCH_ENDPOINT")

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD =os.getenv("APP_PASSWORD")


#print(sheet_data)
#pprint.pprint(sheet_data)

#flight_search = FlightSearch()
data_manager =DataManager(SHEETY_ENDPONT)
#csv_sheet = data_manager.read_file()
flight_details = FlightSearch(KIVI_API,SEARCH_ENDPOINT)
find_row = 0



#get the values
data = data_manager.get_values()
# if data_dict["iataCode"] ==0:
#     print("no value")
customer_email = data_manager.customer_data()  #To get customer Details


sheets_row = 1
for data_dic in data_manager.json_data:


    sheets_row+=1 #start with second row


    iat_code = data_dic.get("iataCode")
    if len(iat_code) == 0:
        code = flight_details.iat_code_finder(data_dic)
        #update code
        data_manager.update(code, sheets_row)
    date_now = dt.date.today()
    date_from = date_now + dt.timedelta(1)
    date_to = date_from + dt.timedelta(days=180)
    date_from_formated = date_from.strftime("%d/%m/%Y")
    date_to_formated = date_to.strftime("%d/%m/%Y")
    fly_to = data_dic["iataCode"]
    flight=flight_details.find_flights(fly_from="LON", fly_to=fly_to, date_from=date_from_formated,
                                       date_to=date_to_formated)
    notification_manager = NotificationManager(BOT_TOKEN,BOT_CHATID)
#
    #if flight is None:
    #    continue
#
    if data_dic["lowestPrice"] >flight.price:
        bot_message = (f"LOW PRICE ALERT \n ONLY {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                       f"to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}")

        print("Message send ")
        if flight.stop_over >0:
            bot_message += (f"\nflight has {flight.stop_over} stop over,via {flight.via_city}.")

        notification_manager.telegram_snd_txt(bot_message)
        notification_manager.send_email(my_email=MY_EMAIL,password=PASSWORD,emails=customer_email,message=bot_message)
        print("message send")