def solution(cars):
    A =[]
    for i in range(0,len(cars)):
        similar = 0
        for j in range(0,len(cars)):
            if i != j:
                cnt =0
                print (cars[i])
                k=0
                while k < len(cars[i]):
                        if cars[i][k] != cars[j][k]:
                            cnt +=1
                            if cnt > 1:
                                break
                        k+=1
                if cnt == 1 or cnt == 0:
                    similar +=1
        A.append(similar)

    return A

cars=['100','110','010','011','100']

print(solution(cars))


