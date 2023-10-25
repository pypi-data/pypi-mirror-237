import requests
import json
import csv


""" 
    curl https://www.melusinapress.lu/api/v1/projects
    Fields: title, subtitle, publicationDate, url
"""

# GET
headers = {'Accept': 'application/json'}
response = requests.get("https://www.melusinapress.lu/api/v1/projects?no_pagination=true", headers=headers)
print(response)
print(response.text)

# Save in json file
with open("melusina_projects.json", "wb") as file:
    file.write(response.content)

# Read json
with open("melusina_projects.json") as f:
    data = json.load(f)

# Extract info
# print(data["data"])
csv_data = []
for s in data["data"]:
    # print(s, type(s))
    title = s["attributes"]["title"]
    subtitle = s["attributes"]["subtitle"]
    pubDate = s["attributes"]["publicationDate"]
    url = "https://www.melusinapress.lu/projects/" + s["attributes"]["slug"]
    col_data = [title, subtitle, pubDate, url]
    print(col_data)
    csv_data.append(col_data)

# Save extracted info into csv
print(csv_data)
column = ["title", "subtitle", "publicationDate", "url"]
with open("melusina_projects.csv", "w", newline="") as csvf:
    writer = csv.writer(csvf, delimiter=";")
    writer.writerow(column)
    writer.writerows(csv_data)
