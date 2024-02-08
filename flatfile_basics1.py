# note! the requests package should be installed in PyCharm before you begin
import csv
import os
import requests

# ignore this, don't edit
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

if not os.path.isfile('favorites.csv'):
    url = 'https://cdn.cs50.net/2023/fall/lectures/7/src7/favorites/favorites.csv'
    filename = 'favorites.csv'
    download_file(url, filename)



# START HERE - this code mirrors CS50x lecture 7 code starting at 11:30
with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])
