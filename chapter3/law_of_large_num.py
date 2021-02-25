# 실전 1-1. 동빈이의 큰 수의 법칙
N,M,K = map(int,input(">> ").split())
num_list = sorted(list(map(int,input(">> ").split())), reverse = True)
result = 0
if N != len(num_list):
    print("Fail! length of list is not equal to N.")

else:
    while M > 0:
        for i in range(K):
            if M <= 0:
                break
            result += num_list[0]
            M -= 1
            # print("M = {}, result = {}, K = {}".format(M,result,K))

        if M <= 0:
            break
        result += num_list[1]
        M -= 1
        # print("M = {}, result = {}, K = {}".format(M,result,K))

    print(result)