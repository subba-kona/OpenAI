import http.client
import re
from datetime import date,timedelta
import geopy
 
today = date.today()+timedelta(days=10)
src_stn = 'PUNE'
print(today)


conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "48f6df45cemshcdaa8c0d3584c98p108ba6jsn4f7d253e5b24",
    'x-rapidapi-host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v1/checkSeatAvailability?classType=3A&fromStationCode={src_stn}&quota=GN&toStationCode=SLO&trainNo=18520&date='2024-10-28'", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))