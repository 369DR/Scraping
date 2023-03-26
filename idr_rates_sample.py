import  requests

# json_data = requests.get("http://www.floatrates.com/daily/idr.json")

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.5960735985312e-5,"date":"Sat, 25 Mar 2023 23:55:01 GMT","inverseRate":15160.534294564},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.128992100322e-5,"date":"Sat, 25 Mar 2023 23:55:01 GMT","inverseRate":16315.896376298}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
