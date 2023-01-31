N = int(input())
origin = N                                                          # 정수 N을 입력받고, N값을 origin에 할당해두고, 출력할 count 변수를 0으로 시작
count = 0

while True :
    try :
        if N < 10 :                                                 # N이 10보다 작다면, test 리스트의 앞에 문자열로 0을 놓고, 뒤에 N을 넣는다.
            test = ['0']
            test += [str(N)]
        else :
            test = list(str(N))                                     # 10보다 크거나 같다면, 각 자리수를 문자열로 바꿔서 test 리스트에 넣는다.
        test_sum = sum(list(map(int,test)))                         # 자리수별로 구분한 것을 map함수로 정수로 바꿔서 합쳐준다. test_sum
        sum_lst = list(str(test_sum))                               # 정수 test_sum을 다시 문자열로 바꾸고, 리스트화해서 자리수별로 구분해준다.
        N = int(str(test[-1]) + str(sum_lst[-1]))                   # 다음 LOOP의 N을 test의 마지막 자리수와, sum_lst의 마지막 자리수를 합친다.
        count += 1                                                  # 횟수 계산 변수인 count에 1을 더해준다.
        if N == origin :         
            print(count)                                            # 만약 현재의 정수 N과 처음 숫자인 origin이 같다면, 현재의 count를 출력해준다.
            break

    except :
        break    

