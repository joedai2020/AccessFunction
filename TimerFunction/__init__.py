import datetime
import logging
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    url = "https://bookingbm-dnbscacuavc7dhbb.eastasia-01.azurewebsites.net/login/"
    response = requests.get(url)

    logging.info(f"访问时间: {datetime.datetime.now()}")
    logging.info(f"状态码: {response.status_code}")
