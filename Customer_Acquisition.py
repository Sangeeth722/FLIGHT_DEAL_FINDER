import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Users/sangeeth/PycharmProjects/EnvironmentVariables/.env.txt")
sheety_end_point_user = os.getenv("SHEETY_ENDPOINT_USER")

def post_sheet():
    end_pont_url = f"{sheety_end_point_user}/flight/user"
    parameters = {
        "user":{
            "firstName":first_name,
            "lastName":last_name,
            "email":email
        }
    }
    response = requests.post(url=f"{end_pont_url}",json=parameters)
    print(response.json())




print("Welcome To Sangeeth's Fight Club")
print("We find the best flights deals and email you")
first_name = input("What is your first name: ")
last_name = input("What is your last name : ")
email = input("What is your email:")
email_confirmation = input("Type your email again :")
if email == email_confirmation:
    post_sheet()
    print("You are in the club")
else:
    print("EMAILS DO NOT MATCH, TRY AGAIN")




