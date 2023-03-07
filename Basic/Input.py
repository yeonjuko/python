# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 데이터의 개수가 적은 수로 정해져 있을 경우
a, b, c = map(int, input().split())
print(a, b, c)