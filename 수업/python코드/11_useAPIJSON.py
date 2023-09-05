import json
import urllib.request
myurl = 'https://api.odcloud.kr/api/3047940/v1/uddi:b7817f63-283f-4857-a34f-bd0e383a6545_201907161308?page=1&perPage=10&serviceKey=I35xhBVrKuRe7RbiQpN9NOkt%2B6JQT5Fd0fgCNDuB0dURcjnYRTmTeyrFaNHFDHVY%2FQ4etMclK24pY%2FdEMx2fGQ%3D%3D'
#web에 있는 데이터를 읽어와서 utf8로 디코딩
response = urllib.request.urlopen(myurl)
response = response.read().decode('utf8')
data = json.loads(response) #text 형태의 data를 json 객체로 바꿈
#쉽게 얘기하면 파이썬의 딕셔너리로 바꾼다고 봐도 됨
#키가 'data'인 것만 가져옴
json_arr = data['data']
for item in json_arr:
    print(f"식당이름:{item['상호명']}, 대표메뉴:{item['주메뉴']}")
    print(f"{item['전화번호']}")