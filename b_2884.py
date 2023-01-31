time = list(map(int,input().split()))       # 입력한 한 줄의 두 숫자를 정수형의 리스트 형식으로 분리

if time[1] >= 45 :                          # 분이 45보다 크거나 같다면 분에서 45를 뺀다
    time[1] -= 45
elif time[1] < 45 :                         # 분이 45보다 작다면 60 - (45 - 분) = 15 + 분으로 분 계산을 해주고
    time[1] = 15 + time[1]                  # 시에선 시가 0이라면 23으로 바꿔주고, 아니라면 1을 빼준다
    if time[0] == 0 :
        time[0] = 23
    else :
        time[0] -= 1

print(time[0], time[1])                     # 시와 분 출력