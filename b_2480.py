dices = list(map(int,input().split()))                  # 입력한걸 리스트 형식으로 분리

if dices[0] == dices[1] == dices[2] :                   # 세 주사위가 같다면 같은 눈 3개 보상인 1번
    prize = 10000 + dices[0] * 1000

elif dices[0] == dices[1] or dices[0] == dices[2] :     # 세 주사위 중 첫번째 주사위와 나머지 중 1개가 같다면 2번 보상에 첫번째 주사위 대입
    prize = 1000 + dices[0] * 100

elif dices[1] == dices[2] :                             # 세 주사위 중 두번째와 세번째가 같다면 2번에 그 값 대입
    prize = 1000 + dices[1] * 100

else :
    largest = 0                                         # 나머지 중에선 가장 높은 값의 주사위를 대입한 3번 보상
    for dice in dices :
        if dice > largest :
            largest = dice
    prize = largest * 100

print(prize)                                            # 보상 출력
