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

information = [('이동준','남성'),('남효정','여성'),('이승봉','여성'),('박예은','여성'),('박유상','남성'),('한신철','남성')]

for item in information:
    print(item)
for a,b in information:
    print(f"이름:{a},성별:{b}")

info = [('이동준','남성','C#'),('안혜선','여성','java')]

for a,b,c in info:
    print("이름:"+a+",성별:"+b+",자신있는언어:"+c)
    print(f"이름:{a},성별:{b},자신있는언어:{c}")