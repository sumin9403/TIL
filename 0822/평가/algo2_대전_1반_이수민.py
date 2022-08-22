# 문제 2번
# import sys; sys.stdin = open('algo2_sample_in.txt','r')

for tc in range(1,int(input()) + 1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    pattern = [list(map(int,input().split())) for _ in range(3)]

    n = N - 3 + 1                       # 비교해야할 테이블의 범위
    result = 0                          # 결과 값
    for r in range(n):              # 찾으려는 테이블의 범위 : r, c
        for c in range(n):
            for pr in range(3):         # 찾고자 하는 패턴의 범위 : pr, pc
                break_point = 0         # 비교 중간에 다른 부분이 있으면 빠져나오기 위한 변수
                for pc in range(3):
                    if table[r+pr][c+pc] != pattern[pr][pc]:
                        break_point = 1                         # 열 비교 중 다른 부분이 나오면 멈추고 break_point = 1로 지정
                        break
                if break_point:                                 # break_point가 0이 아니면 빠져나가라
                    break
            else:
                result += 1                                     # for 문이 이상 없이 수행됐으면 모두 같으므로 result에 1을 더하기

    print(f'#{tc}',result)
