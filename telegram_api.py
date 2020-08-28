import requests
token = '262238046:AAFq-ngBq5Dw2I5GnMMSWAG8s1UxkRfKu2Q'
url = f'https://api.telegram.org/bot{token}/getUpdates'
requests.post(url).json()