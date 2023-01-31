import sys

test_case = int(input())                                                    # 입력 받으면

for num in range(test_case) :
    testsum = sum(list(map(int,sys.stdin.readline().rstrip().split())))     # sys.stdin.readline()으로 읽고, rstrip()으로 공백 제거한 뒤, split()으로 분리
    print(testsum)                                                          # 그 뒤 map함수로 리스트의 두 요소들을 정수로 바꿔준 뒤, 다시 리스트화해서 합하고 출력