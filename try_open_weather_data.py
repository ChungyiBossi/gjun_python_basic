import requests
from pprint import pprint

address = '臺北市中正區公園路'
code = 'CWA-30010294-FD42-486A-84EF-094F518DD29C'
url = f'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON'
f_data = requests.get(url)  # 取得主要縣市預報資料
f_data_json = f_data.json()  # json 格式化訊息內容

stations = f_data_json['cwaopendata']['dataset']['Station']
pprint(len(stations))

for station in stations:
    station_name = station["StationName"].strip()
    county_name = station["GeoInfo"]["CountyName"].strip()
    town_name = station["GeoInfo"]["TownName"].strip()
    # print(county_name, town_name)
    # if county_name in address:
    if county_name in address and town_name in address:
        print(station_name, county_name, town_name)
        pprint(station['WeatherElement'])