# 실전 7-2. 떡볶이 떡 만들기: 길이가 일정하지 않은 N개의 떡을 H cm로 자를 수 있는 절단기를 이용해 자른다. 이때, 잘려진 떡의 길이 총합이 M이 되도록하는 H는?
# 이 버젼은 이진탐색을 사용해보았습니다.
def binary_tree(num, lst, start, end):  # 입력받은 떡의 길이가 1000000까지 커질 수 있으므로 sort와 binary_tree 조합으로 구하였음.
    mid = (start+end)//2    # 이진탐색을 위해 binary_tree function을 갖고 왔으나, 이를 수정해야합니다.. 하지만 다른 문제 먼저 풀고 오겠습니다.
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

NM = list(map(int, input(">> ").split()))
N,M = NM[0], NM[1]
lst = sorted(list(map(int, input(">> ").split())), reverse=True)
memo = {}
result = 0
H = max(lst)
for num in lst:
    if not num in memo:
        memo[num] = 1
    else:
        memo[num] += 1