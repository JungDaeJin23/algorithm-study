# 다른 사람 아이디어
N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for idx in range(1, len(arr)):
    if arr[idx] > dp[-1]:
        dp.append(arr[idx])
    else:
        jdx = len(dp)-2
        # 더 뒤에오는 숫자가 앞에 올 수 도 있음 하지만 이는 앞으로 더 긴 부분 수열이 올 수 도 있을 것에 대한 대비이지
        # 현재의 가장 긴 부분 수열의 길이랑은 아무 상관이 없음
        # 가장 긴 부분 수열을 구하는 식에서는 통하지 않음
        while jdx >= 0:
            if arr[idx] < dp[jdx]:
                dp[jdx] = arr[idx]
                break
            jdx -= 1

print(len(dp))