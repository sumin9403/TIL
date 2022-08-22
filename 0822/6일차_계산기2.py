def pop():
    global top
    top -= 1
    return stack[top+1]         # 마지막 값을 return

def push(x):
    global top
    top += 1                    # top += 1을 해주고 넣어야 stack[top]이 마지막 원소를 가리킴
    stack[top] = x
    return

# =============================================  계산기 1 : 중위 표기법 -> 후위 표기법

icp = {'(': 3, '*':2, '/' : 2, '+':1,'-':1,')':4}       # in-coming priority
isp = {'(': 0, '*':2, '/' : 2, '+':1,'-':1,')':4}       # in-stack priority

for tc in range(1,11):
    N = int(input())
    infix = input()
    postfix = []                # 데이터를 저장할 list : 숫자는 바로 저장, 연산자는 stack에 저장 후 순서에 맞게 저장될 것
    top = -1
    stack = [0]*N               # 연산자를 임시 저장할 stack 생성
    for alpha in infix:
        if alpha in icp:        # 숫자인지 연산자인지 판별 숫자이면 바로 else 구문에 들어간다.
            if top < 0 and icp[alpha] < 4:      # stack에 저장된 값이 아무것도 없고, 닫는 괄호가 아닌 기호면 바로 push
                push(alpha)                     # top이 -1 인 경우 비교하면 index error가 발생해서 해당 조건을 만들었음
            elif icp[alpha] == 4:               # alpha가 닫는 괄호( ")" ) 일 경우
                while isp[stack[top]] != 0:     # stack이 여는 괄도( "(" ) 가 나올 때 까지 postfix에 저장
                    postfix += [pop()]
                pop()                           # 여는 괄호는 버림
            elif icp[alpha] > isp[stack[top]]:      # 들어오는 기호의 우선순위가 스택에 있는 기호의 우선 순위보다 높으면 저장
                push(alpha)
            elif icp[alpha] <= isp[stack[top]]:     # 들어오는 기호의 우선순위가 스택에 있는 기호의 우선 순위보다 낮으면 빼내고 저장
                while top != -1 and icp[alpha] <= isp[stack[top]]:
                    postfix += [pop()]
                push(alpha)
        else:                   # 숫자는 postfix에 바로 저장
            postfix += [alpha]
    else:
        while top != -1:
            postfix += [pop()]

#=========================================== 계산기 2 : 후위 표기법 식 계산
    calcul_stack = []
    for alpha in postfix:
        if alpha in icp:                        # 연산자는 스택에 저장된 최근 두 숫자를 연산 후 그 값을 저장
            if alpha == '-':
                num2, num1 = pop(), pop()       # 먼저 들어온 값이 상대적으로 나중에 나오기 때문에 num2, num1 = pop(), pop()
                new_num = num1 - num2
                push(new_num)                   # 연산한 결과 값을 저장
            elif alpha == '+':
                num2, num1 = pop(), pop()
                new_num = num1 + num2
                push(new_num)
            elif alpha == '*':
                num2, num1 = pop(), pop()
                new_num = num1 * num2
                push(new_num)
            else:
                num2, num1 = pop(), pop()
                new_num = num1 // num2
                push(new_num)
        else:
            push(int(alpha))            # 숫자는 타입을 변환해서 stack에 저장

    print(f'#{tc}',stack[top])          # 최종 결과는 stack의 top 즉 0번 인덱스에 저장됨.