import requests

url = 'https://duckduckgo.com/presidents of the united states/?q=DuckDuckGo&format=json'

response = requests.get(url)

json_data = response.json()


president_list = []

for president in json_data:
    print(json_data['RelatedTopics'])

#print(president_list)
