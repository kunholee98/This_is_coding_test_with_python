# 3. 시각 문제
times_with_3 = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]    # 3이 들어간 모든 경우의 리스트. 변수에 들어갈 수 있는 최대값이 60이므로 그 이하인 수들.
N = int(input(">> "))
count = 0
for hour in range(N+1):
    if hour in times_with_3:    # 만약 hour에 3이 들어가 있다면 분, 초에 관계없이 카운팅을 해야하므로 3600을 더해줌.
        count += 60*60
    else:
        for minute in range(60):    # 만약 minute에 3이 들어가 있다면 초에 관계없이 카운팅을 해야하므로 60을 더해줌.
            if minute in times_with_3:
                count += 60
            else:
                for second in range(60):    # 만약 second에 3이 들어가 있다면 카운트.
                    if second in times_with_3:
                        count += 1
print(count)