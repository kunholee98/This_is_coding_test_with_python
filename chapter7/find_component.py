# 실전 7-1. 부품 찾기: N개의 부품을 가지고 있을 때, M개의 부품 요청에 맞는 부품들이 있는지 확인하여 y/n로 대답하기.
def binary_tree(num, lst, start, end):  # 입력받은 n_lst의 크기가 1000000까지 커질 수 있으므로 sort와 binary_tree 조합으로 구하였음.
    mid = (start+end)//2
    #print(num,start,end,mid)
    if num == lst[mid]:
        return "yes"
    elif start > end:
        return "no"
    elif num > lst[mid]:
        #print("num > mid")
        #print(num,lst[mid])
        return binary_tree(num,lst,mid+1,end,)
    elif num < lst[mid]:
        #print("num < mid")
        end = mid
        mid = (start+end)//2
        return binary_tree(num,lst,start,mid-1)

N = int(input(">> "))
n_lst = sorted(list(map(int, input(">> ").split())))
M = int(input(">> "))
m_lst = list(map(int, input(">> ").split()))
result = []
for num in m_lst:
    result.append(binary_tree(num,n_lst,0,N-1))
print(' '.join(result))