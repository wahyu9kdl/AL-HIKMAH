import requests

url = "https://www.alhikmah.my.id/2022/02/kitab_28.html"


resp = requests.get(url)

print(resp.status_code)
