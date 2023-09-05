import json
import urllib.request

myurl = 'https://api.odcloud.kr/api/3047940/v1/uddi:b7817f63-283f-4857-a34f-bd0e383a6545_201907161308?page=1&perPage=10&serviceKey=MgX2EIv5i2myv26gGKACE9U5XFuLIi%2BggnKqN8I0BaN4mpFOsHCmqIopmOqpyukSrphm6MrV0aY0Nf4YVB3ceA%3D%3D'

response = urllib.request.urlopen(myurl)
response = response.read().decode('utf8')
#print(response)

data = json.loads(response)

json_arr = data['data']

for item in json_arr:
    print(f"식당이름:{item['상호명']}, 대표메뉴:{item['주메뉴']}, 전화번호:{item['전화번호']}")