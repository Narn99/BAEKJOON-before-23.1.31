now_time = list(map(int,input().split()))           # 현재 시간을 리스트 형식으로 입력

cooking_time = int(input())                         # 요리하는 시간

if now_time[1] + cooking_time >= 60 :
    now_time[0] += (now_time[1] + cooking_time) // 60   # 현재 시간의 분과 요리 시간을 합친게 60을 넘는다면, 60으로 나눈 몫을 시에 추가
    now_time[1] = (now_time[1] + cooking_time) % 60     # 그리고 60으로 나눈 나머지를 분으로 할당
else :
    now_time[1] += cooking_time                         # 그 외에는 합쳐도 60분을 안 넘기니 그냥 분과 요리 시간을 합쳐준다.
if now_time[0] >= 24 :
    now_time[0] -= 24                                   # 만약 시가 24시를 넘긴다면 24를 빼준다.

print(now_time[0], now_time[1])