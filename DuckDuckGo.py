import requests

url = 'https://duckduckgo.com/presidents of the united states/?q=DuckDuckGo&format=json'

response = requests.get(url)

json_data = response.json()


president_list = []

for president in json_data:
    president_list.append(json_data['RelatedTopics'])
# I have no idea RelatedTopics is blank it also show up on the website as blank when you inspect element
print(president_list)
