import pprint
import requests
import pandas as pd

file_path = "flight_check - Sheet1.csv"
class DataManager:
    def __init__(self,end_point):
        self.end_pont = end_point


    def get_values(self,):
        response = requests.get(url = f"{self.end_pont}/sheet1")
        data_json = response.json()["sheet1"]
        self.json_data = data_json

    def update(self,code,positiion):
        end_pont_url = f"{self.end_pont}/{positiion}"
        parameters = {"sheet1": {
                    "iataCode":code,

                }
                             }
        response = requests.put(url = end_pont_url,json=parameters)
    def customer_data(self):
        response = requests.get(url=f"{self.end_pont}/user")
        data_json = response.json()["user"]
        return data_json





