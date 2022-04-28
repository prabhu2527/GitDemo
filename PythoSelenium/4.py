#Maximum binary Gap in a integer
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    B=decimalToBinary(N)

    Final=[]
    index =0

    while index < len(B):
        cnt = 0
        #print (B[index])
    #for index in range(len(B)):
        if B[index] == '1':
            #print("hi")
            start_index = index
            k=start_index+1
            #for k in range(start_index+1,len(B)):
            while k < len(B):
                if B[k]=='1':
                    break
                elif B[k]=='0':
                    cnt +=1
                k +=1
            #print (len(B)-1)
            #print(k)
            if k == len(B) and B[k-1] == '0':
                cnt=0
                Final.append(0)
                break
            else:
                index = k
            Final.append(cnt)
        else:
            index +=1
    C= sorted(Final)
    return(C[-1])

def decimalToBinary(n):
    return bin(n).replace("0b", "")

solution(9)




#solution(1041)