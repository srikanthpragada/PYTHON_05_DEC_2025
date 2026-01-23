import requests

user = "gvanrossum"
url = f"https://api.github.com/users/{user}"

resp = requests.get(url)

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

details = resp.json()   # Convert JSON to dict

print('Name    : ', details['name'])
print('Company : ', details['company'])
print('Location: ', details['location'])
print('Create  : ', details['created_at'])




