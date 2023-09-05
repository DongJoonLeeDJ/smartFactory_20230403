numberlist = [1,2,3,4,5]
#enumerate : 리스트, 튜플, 문자열의 인덱스와 해당 값 반환
for index, value in enumerate(numberlist):
    print('idx:'+str(index))
    print('value:'+str(value))
    print(f'index={index},value={value}')
sentense="안녕하세요."
for i,v in enumerate(sentense):
    print(f'sentense[{i}]={v}')
#find : 특정 문자열의 시작 인덱스를 찾기 위해서 사용
print(sentense.find("하세")) # 2 (세번째에 하가 시작되고 하세가 됨)
print(sentense.find("이동준")) # -1 (없는 거)

#filter : 함수를 이용해서 필터링을 함
#함수에 만족하는 값들만 반환을 해 줌
numberlist = numberlist + [6,7,8,9,10]
print(numberlist)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def isOdd(n):
    return n%2==1 
#isOdd 에서 True를 반환할 수 있는 값만 가져옴
oddlist = list(filter(isOdd, numberlist))
print(oddlist)

#lambda : 익명 함수, 한 줄 짜리 함수라고 봐도 됨
#콜백 함수에서 주로 사용됨
#따로 함수를 만들지 않아도 즉석에서 쓸 수 있음
#콜백 함수 : 함수의 매개변수로 이용되는 함수
check_even = lambda x : x%2==0
#x : 매개변수
#x%2==0 : 리턴값
evenList1 = list(filter(check_even,numberlist))
evenList2 = list(filter(lambda x : x%2==0,numberlist))
#x는 numberlist에 있는 숫자들
print(evenList1)
print(evenList2)

powerList = list(map(lambda x: x**3, numberlist))
print(numberlist)
print(powerList)
