x = int(input())
y = int(input())                # x와 y값 입력

if x > 0 :
    if y > 0 :
        print('1')              # 둘 다 양수라면 1 사분면
    elif y < 0 :
        print('4')              # x는 +, y는 -라면 4사분면
elif x < 0 :
    if y > 0 :
        print('2')              # x는 -, y는 +라면 2사분면
    elif y < 0 :
        print('3')              # 둘 다 음수라면 3사분면
    