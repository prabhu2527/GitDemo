def solution(A):
    # write your code in Python 3.6
    B=sorted(A)
    print(B)
    initial_value = B[0]
    for i in B:
        if i != initial_value:
            if i <= 0:
                return 1
            elif i == B[-1]:
                initial_value+=1
                return initial_value +1
            else:
                return initial_value
        else:
            initial_value +=1

A=[1,2,3]
print(solution(A))