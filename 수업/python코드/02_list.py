list1 = [1,2,3,4,5] #정수 리스트
list2 = [1.0,3.14,2.0] #실수 리스트
list3 = [34,3.14,'이동준',list1,list2] #여러 타입이 저장되는 리스트
#range(1,11) : 1부터 10까지의 값
list4 = list(range(1,11)) #1부터 10까지의 리스트
print(list1)
print(list2)
print(list3)
print(list4)
#문자열 자체를 문자 리스트로 취급한 것
print("123"[0]) # 가장 첫번째 자리 문자열 출력
print("123"[1])

mylist = [1,2,3,4,5,6,7,8,9,10] #가장 첫번째는 [0]
test1 = mylist[-1] # 10
print(test1)
test2 = mylist[2:] # [3, 4, 5, 6, 7, 8, 9, 10]
print(test2)
test1 = mylist[-2:] # [9, 10]
print(test1)
test3 = mylist[1:-2]
print(test3)
mylist[4] = 500
print(mylist)
#index 범위를 주의할 것
#mylist는 [0]~[9]까지 총 10개의 값이 있음
#[10]번째 값은 존재하지 않음
#mylist[10] = 1000 #IndexError: list assignment index out of range

mylist.append(1000) #끝에 값 추가
mylist.insert(4,555) # [4]번째에 값을 중간에 삽입
mylist = mylist + [111]
mylist = mylist + [222,333,4444]
print(mylist)

#pop : 값을 빼옴
#del : 값 자체를 지워버림
a = mylist.pop() #끝에 껄 삭제하고 a에다가 값을 대입
print(a)
print(mylist)
b = mylist.pop(0) #첫번째껄 삭제하고 b에다가 값을 대입
print(b)
print(mylist)
del mylist[0] # 삭제
print(mylist)
print(len(mylist)) #리스트의 길이

# 튜플 
#리스트랑 똑같은 데 소괄호를 씀
# 값 수정 불가능
tuple1 = (1,2,3,4,5)
#tuple1[0] = 100 #'tuple' object does not support item assignment
tuple1 = tuple1 + (100,) #튜플끼리 합치는 건 됨
print(tuple1)