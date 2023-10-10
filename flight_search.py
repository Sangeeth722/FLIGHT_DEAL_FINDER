import requests
from flight_data import FlightData
import pprint



class FlightSearch:


#This class is responsible for talking to the Flight Search API
    def __init__(self,api,end_pont):
        self.api = api
        self.endpoint = end_pont


    def iat_code_finder(self,dict):
        parameter = {

            "term":dict["city"],
        }

        header = {
            "apikey":self.api,
        }

        response = requests.get(url=f"{self.endpoint}/locations/query",params=parameter,headers=header)
        code = response.json()["locations"][0]["code"]

        return code
    def find_flights(self, fly_from, fly_to, date_from, date_to):

        header = {
            "apikey": self.api
        }
        parameter = {
            "fly_from":fly_from,
            "fly_to":fly_to,
            "date_from":date_from,
            "date_to":date_to,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "one_for_city":1,
            "max_stopovers": 0,
            "curr":"GBP"

        }

        response = requests.get(url = f"{self.endpoint}/v2/search",params=parameter,headers=header)
        response_json = response.json()

        try:
            price = response_json["data"][0]["price"]

        except IndexError:
            parameter["max_stopovers"] = 2
            response = requests.get(url=f"{self.endpoint}/v2/search", params=parameter, headers=header)
            data = response.json()
            route = data["data"][0]["route"]
            flight_data = FlightData(price=data["data"][0]["price"], origin_city=route[0]["cityFrom"],
                                     origin_airport=route[0]["cityCodeFrom"], destination_city=data["data"][0]["cityTo"], destination_airport=
                                     data["data"][0]["cityCodeTo"], out_date=route[0]["local_departure"].split("T")[0],
                                     return_date=route[2]["local_departure"].split("T")[0],
                                     stop_overs=1,via_city=route[0]["cityTo"])

            return flight_data





        else:
            orgin_city = response_json["data"][0]["cityFrom"]
            orgin_airport = response_json["data"][0]["flyFrom"]
            destination_city = response_json["data"][0]["cityTo"]
            destination_airport = response_json["data"][0]["flyTo"]
            out_data = response_json["data"][0]["route"][0]["local_departure"].split("T")[0],
            return_date = response_json["data"][0]["route"][1]["local_departure"].split("T")[0]

            flight_data = FlightData(price,orgin_city,orgin_airport,destination_city,destination_airport,out_data,return_date)



            return flight_data










