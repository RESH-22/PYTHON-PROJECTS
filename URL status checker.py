import requests

sites = ["https://google.com", "https://github.com"]

for site in sites:
    r = requests.get(site)
    print(site, r.status_code)
