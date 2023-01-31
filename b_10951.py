import sys                                                                  # sys 모듈 사용

while True :
    try :
        a, b = list(map(int,sys.stdin.readline().rstrip().split()))          # 입력받은 글을 분리해서 map함수를 써서 정수로 바꾼 뒤 리스트화
        print(a + b)                                                         # 반복마다 만든 리스트의 합을 출력

    except :                                                                    # 예외 발생 시 종료
        break