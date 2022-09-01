import requests
import urllib3

url = "https://europe-west2-liquid-optics-354223.cloudfunctions.net/get_fib_sequence?iteration=50000"

payload = {}
headers = {}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text.encode('utf8'))


response = requests.post(url)
print(response.text)
