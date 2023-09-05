myinfo = True
# 조건 끝에 콜론(:) 꼭 붙이기
# 들여쓰기 필수(스페이스 바 4칸)
if myinfo:
    print("이 정보는 사실입니다.")
info = 10>100 # 거짓
if info:
    print("이 건 절대 출력 안 됨")
age = 34
#and 혹은 &를 사용해서 다양한 조건문을 작성할 수도 있다.
#or 혹은 |를 사용해서 다양한 조건문을 작성할 수도 있다.
# |의 정체 : shift + \
if age>=30 and age<40:
    print("30대입니다.")
if age>0 or age<100:
    print("일반적인 연령대입니다.")

age = 40
if age < 20:
    print("미성년자")
elif age < 40:
    print("40살 미만")
else:
    print("age="+str(age))
    print("age={}".format(age))
    print("age=%d"%age)
    print(f"age={age}")

if age==0:
    print('age=0')
elif age==40:
    print("age는 40")
#else 없이 elif로 끝내도 상관없다
#다른 언어들도 else if로 끝나도 상관없듯이
#파이썬도 elif로 끝나도 상관없음
