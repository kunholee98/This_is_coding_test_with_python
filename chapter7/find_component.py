# 실전 7-1. 부품 찾기: N개의 부품을 가지고 있을 때, M개의 부품 요청에 맞는 부품들이 있는지 확인하여 y/n로 대답하기.
def binary_tree(num, lst, start, end, mid):
    print(num,start,end,mid)
    if num == lst[mid]:
        return "yes"
    elif start == end:
        return "no"
    elif num > lst[mid]:
        print("num > mid")
        print(num,lst[mid])
        start = mid
        mid = (start+end)//2+1
        return binary_tree(num,lst,start,end,mid)
    elif num < lst[mid]:
        print("num < mid")
        end = mid
        mid = (start+end)//2
        return binary_tree(num,lst,start,end,mid)

N = int(input(">> "))
n_lst = sorted(list(map(int, input(">> ").split())))
M = int(input(">> "))
m_lst = list(map(int, input(">> ").split()))
print(binary_tree(m_lst[0],n_lst,0,N-1,(N-1)//2))