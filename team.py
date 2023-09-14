# 평균을 구하는 함수
def f_avg(data): # 최준호 수정
    result = sum(data) / len(data)
    return result

# 합계를 구하는 함수
def f_sum(data):
    return sum(data)

# 오름차순으로 정렬해주는 함수
def f_sort(data) :
    return data.sort()

# 내림차순으로 정렬해주는 함수
print(f_avg([1, 2, 3, 4, 5]))