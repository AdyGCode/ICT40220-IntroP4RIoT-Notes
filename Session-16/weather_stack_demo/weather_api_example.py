import http.client
from dotenv import load_dotenv
import os

load_dotenv()

WEATHERSTACK_APIKEY = os.getenv('WEATHERSTACK_KEY')
WEATHERSTACK_HOST=os.getenv('WEATHERSTACK_HOST')
LOCATION = "Perth,Australia"

conn = http.client.HTTPSConnection(WEATHERSTACK_HOST)

request_string = f"/current?access_key={WEATHERSTACK_APIKEY}?query={LOCATION}"

print("http://"+WEATHERSTACK_HOST+request_string)

conn.request("GET", request_string)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))