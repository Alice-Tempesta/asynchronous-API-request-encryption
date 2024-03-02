import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()
global_api_key = os.environ.get('RANDOM_TEXT_API_KEY')


def get_random_text():
    url = "https://randommer.io/api/Text/LoremIpsum?loremType=normal&type=words&number=5"
    headers = {"X-Api-Key": global_api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        random_text = response.text
        return random_text
    else:
        print(f"Error getting text. Response code: {response.status_code}")

    return ""


def generation_text():

    random_text = get_random_text()
    return (random_text)
