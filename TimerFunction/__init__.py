import datetime
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    url = "https://bookingbm-dnbscacuavc7dhbb.eastasia-01.azurewebsites.net/login/"
    response = requests.get(url)
