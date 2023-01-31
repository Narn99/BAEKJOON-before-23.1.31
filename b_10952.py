import sys                                                                  # sys 모듈 사용

while True :
    testlst = list(map(int,sys.stdin.readline().rstrip().split()))          # 입력받은 글을 분리해서 map함수를 써서 정수로 바꾼 뒤 리스트화
    if testlst == [0, 0] :                                                  # 입력 받은게 만약 0 두 개라면 반복문 종료
        break 
    print(sum(testlst))                                                     # 반복마다 만든 리스트의 합을 출력