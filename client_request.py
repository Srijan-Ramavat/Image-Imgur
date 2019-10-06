# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:8000/image"

# image location given here
location = "image/images.jpg"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'image': location}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

print(data)
