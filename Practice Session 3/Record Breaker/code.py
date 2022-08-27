def record_breaker():
    N = input()
    V = list(map(int, input().split()))
    
    record_breaking_days = 0
    max_visitors = -1
    
    for i in range(len(V)):
        if i == 0 or V[i] > max_visitors:
            max_visitors = V[i]
            if i == len(V) - 1 or V[i] > V[i + 1]:
                record_breaking_days += 1
    
    return record_breaking_days


T = int(input())
for test_case_no in range(1, T + 1):
    print(f"Case #{test_case_no}: {record_breaker()}")