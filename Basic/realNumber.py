# 소수부가 0일 때 0을 생략
a = 5.
print(a) # 5.0

# 정수부가 0일 때 0을 생략
a = -.7
print(a) # -0.7

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)