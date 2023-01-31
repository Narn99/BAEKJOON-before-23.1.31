import sys

test_case = int(input())                                                    # 입력 받으면

for num in range(test_case) :
    testlst = list(map(int,sys.stdin.readline().rstrip().split()))          # sys.stdin.readline()으로 읽고, rstrip()으로 공백 제거한 뒤, split()으로 분리하고 map함수로 정수로 바꿔서 리스트로 할당
    testsum = sum(testlst)
    print(f'Case #{num+1}: {testlst[0]} + {testlst[1]} = {testsum}')        # 리스트 요소들을 합한 값과 그 요소들을 이용해서, 해답을 f-string으로 문장 다듬어서 출력