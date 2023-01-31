N = int(input())            # 수를 입력받으면,

for num in range(N) :       # 그 수만큼 줄마다 *을 1개씩 늘려가며 출력, sep=''로 글자 사이의 띄어쓰기를 없앤다.
    print(' '*(N-(num+1)),'*'*(num+1),sep = '')