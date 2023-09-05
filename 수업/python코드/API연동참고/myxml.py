import xml.etree.ElementTree as elemTree
import requests

myurl = 'https://api.odcloud.kr/api/3047940/v1/uddi:b7817f63-283f-4857-a34f-bd0e383a6545_201907161308?page=1&perPage=10&returnType=XML&serviceKey=MgX2EIv5i2myv26gGKACE9U5XFuLIi%2BggnKqN8I0BaN4mpFOsHCmqIopmOqpyukSrphm6MrV0aY0Nf4YVB3ceA%3D%3D'

response = requests.get(myurl)

xmldatas = elemTree.fromstring(response.text)

myresult = xmldatas.find('data').findall('item')

for item in myresult:
    print("식당명 : " + item.find('./col[@name="상호명"]').text + ", 주메뉴 : " + item.find('./col[@name="주메뉴"]').text+", 전화번호 : " + item.find('./col[@name="전화번호"]').text)    