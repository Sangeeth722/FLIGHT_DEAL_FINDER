import requests
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

        def __init__(self, bot_token, chatId):
            self.bot_token = bot_token
            self.bot_chatId = chatId


        def telegram_snd_txt(self, bot_message):
            send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatId + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(send_text)
            self.json = response.json()

        def send_email(self,my_email,password,emails,message):
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                #we got list a Json data list,, So decode to find user emails via loops
                for item in emails:
                    email = item["email"]


                    connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject :Flight Deal \n\n {message}")



