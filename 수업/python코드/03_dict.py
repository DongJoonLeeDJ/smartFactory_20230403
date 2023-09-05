djlee = {
    'name' : '이동준',
    'gender' : '남',
    'lang' :  {
           'speak' : ['kor','eng','jpn'],
            'coding' : ['c','c#','java','python']
    },
    '나이' : 34,
    0 : '가정의 평화'
}
print(djlee)
print(djlee[0])
print(djlee['나이'])
#새로운 키를 추가하는 방법이 매우 쉽다.
#그냥 대입하면 됨
#리스트였다면 없는 부분에 값을 넣는 게 되므로 오류가 났을 것
#딕셔너리는 바로 해당 키를 생성하고 거기에 값을 추가해 줌
djlee['birth'] = '19890430'
print(djlee['birth'])
del djlee['나이']
del djlee['lang']
print(djlee) #{'name': '이동준', 'gender': '남', 0: '가정의 평화', 'birth': '19890430'}


#True 랑 False (Boolean 자료형)
print(1==1) # True
print(1!=1) # False
