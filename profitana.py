def getMinimumCost(cost, k):
    n = len(cost)
    
    # 제약 조건 검증
    if not (1 <= k <= n <= 2 * 10**5):
        return 0
    if not all(1 <= x <= 10**7 for x in cost):
        return 0
        
    # dp[i]: i번째 지점까지 도달하는데 필요한 최소 비용
    dp = [float('inf')] * n
    dp[0] = 0  # 시작점의 비용
    
    # 각 지점에 대해
    for i in range(1, n):
        # j에서 i로 점프하는 경우를 고려
        for j in range(max(0, i-k), i):
            # j에서 i로 점프할 때의 비용 = j까지의 최소비용 + i지점의 cost
            dp[i] = min(dp[i], dp[j] + cost[i])
    
    return dp[n-1]

# 입력 처리
n = int(input())  # 점의 개수
cost = list(map(int, input().split()))  # 각 지점의 비용
k = int(input())  # 최대 점프 길이

# 결과 출력
print(getMinimumCost(cost, k))

def findConsistentLogs(userEvent):
    n = len(userEvent)
    
    # 제약 조건 검증
    if not (1 <= n <= 2 * 10**5):
        return 0
    if not all(1 <= x <= 10**5 for x in userEvent):
        return 0
    
    def get_frequency_info(arr):
        # 배열에서 각 요소의 빈도수를 계산하고 최소/최대 빈도수 반환
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        if not freq:
            return 0, 0
        return min(freq.values()), max(freq.values())
    
    # 전체 배열의 최소 빈도수 계산
    min_freq, _ = get_frequency_info(userEvent)
    
    max_length = 0
    # 모든 가능한 시작점에 대해
    for start in range(n):
        freq = {}
        # 시작점부터 끝까지 확장
        for end in range(start, n):
            # 현재 요소 추가
            freq[userEvent[end]] = freq.get(userEvent[end], 0) + 1
            
            # 현재 부분 배열의 최대 빈도수가 전체 배열의 최소 빈도수와 같은지 확인
            curr_min, curr_max = min(freq.values()), max(freq.values())
            if curr_max == min_freq:
                max_length = max(max_length, end - start + 1)
    
    return max_length

# 입력 처리
n = int(input())  # 이벤트 로그 크기
userEvent = list(map(int, input().split()))  # 사용자 이벤트 로그

# 결과 출력
print(findConsistentLogs(userEvent))
