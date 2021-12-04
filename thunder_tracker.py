import requests
import boto3
import pprint
import re
import os 

load_dotenv()

def lambda_handler(event, context):
    api_key = os.getenv("API_KEY")
    location = os.getenv("LOCATION")
    aws_account = os.getenv("AWS_ACCOUNT")

    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:{aws_account}:thunder_warning')

    url= 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location}?apikey={api_key}'

    thunder_warning = [15,16,17,41,42]
    animal_name = "Alfie"
    results = requests.get(url)
    results = results.json()

    for result in results:
        event_time = result['DateTime']
        event_time = re.search('(?<=T).+(?=\+)', event_time)
        event_time = event_time.group(0)
        summary = result['IconPhrase']
        weather_id = result['WeatherIcon']

        if weather_id in thunder_warning:
            topic.publish(
                Subject="Thunder Warning!", 
                Message=f"Bring shinker inside before {event_time}! {summary} predicted."
            )
            print(f"Bring {animal_name} inside before {event_time}! {summary} predicted.")
            print("Warning sent!")
            return
