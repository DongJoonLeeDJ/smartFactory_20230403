# while, for

#break : 반복문 끝내기
#continue : 해당 단계를 건너뜀

count = 0
while count<100:
    count += 1
    if count%2==0: #짝수인 경우
        continue #현재 단계 스킵
    if count>50:
        break #반복문 끝남
    print(f"count={count}")
print("count="+str(count)) #51


for item in range(1,101):
    if item % 2 ==0:
        continue
    if item > 50:
        break
    print(f"item={item}")
print(item)
print(item)