# 문제 1번 평지만들기
# import sys; sys.stdin = open('algo1_sample_in.txt','r')

for tc in range(1,int(input())+1):
    N = int(input())
    y1,x1,y2,x2 = map(int,input().split())  # 여기 변수 설정 잘못해서 틀렸음
    table = [list(map(int,input().split())) for _ in range(N)]

    table_sum = 0                           # 원하는 영역의 합 계산
    cnt = 0                                 # 평균 계산하기 위해 요소 개수 구하기
    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            table_sum += table[r][c]
            cnt += 1

    table_average = table_sum//cnt          # 평균값 구하기 (조건 : 정수 & 내림)
    result = 0                              # 작업 횟수 구하기
    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            substacne = table_average - table[r][c]                     # 칸의 숫자와 평균값 차이 즉 그 칸의 작업 횟수
            result += substacne if substacne >= 0 else -1 * substacne   # 차이가 음수인 경우 -1 곱해서 양수로 바꾸기

    print(f'#{tc}', result)