try:
    a=10
    b=1
    print(f"a={a},b={b}")
    c=a/b
    print(c)
except Exception as e:
    print(e)
    exit()
print("졸면 안 됩니다.")


try:
    a=10
    b=0
    print(f"a={a},b={b}")
    c=a/b
    print(c)
except Exception as e:
    print(e)
    exit()
finally:
    print("이건 반드시 출력함~~~~~~")
print("졸면 안 됩니다.")