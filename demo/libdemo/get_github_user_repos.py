import requests

user = "gvanrossum"
url = f"https://api.github.com/users/{user}/repos"

resp = requests.get(url)

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

repos = resp.json()  # Convert JSON to list[dict]

for repo in repos:
    print(repo['name'])
    print(repo['description'])
    print('-' * 80)
