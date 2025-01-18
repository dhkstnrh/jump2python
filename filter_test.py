# 양수 값만 리턴

def filter_test1(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

def filter_test2(x):
    return x > 0

print("양수 값 판별\n입력 예시: 1 -3 2 0 -5 6 \n")

print("결과: ", filter_test1([1, -3, 2, 0, -5, 6]))

# 사용자 입력
try:
    user_input = list(map(int, input("값을 입력하세요: ").split()))
    print("사용자 입력: ", filter_test1(user_input))
except ValueError:
    print("Please enter valid integers separated by spaces.")

# filter(함수, 반복 가능한 데이터)
print("filter 함수 사용 결과: ", list(filter(filter_test2, [1, -3, 2, 0, -5, 6])))

# lambda 응용
print("lambda 결과: ", list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))