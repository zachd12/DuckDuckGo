import requests

url ="https://api.duckduckgo.com"

response = requests.get(url)

json_data = response.json()

president_list = []

for president in json_data:
    president_list.append








