# 실전 7-2. 떡볶이 떡 만들기: 길이가 일정하지 않은 N개의 떡을 H cm로 자를 수 있는 절단기를 이용해 자른다. 이때, 잘려진 떡의 길이 총합이 M이 되도록하는 H는?
# 이 버젼은 이진탐색을 사용해보았습니다.
def binary_tree(num, lst, start, end):  # 입력받은 떡의 길이가 1000000까지 커질 수 있으므로 sort와 binary_tree 조합으로 구하였음.
    mid = (start+end)//2                # 문제에 대한 설명은 tteokbokki.py 에서 확인하시길!
    sum = 0
    for i in lst:
        if i > mid:
            sum += i-mid
    print(start, mid, end,sum)
    if sum == M:
        return mid
    elif sum > M:
        return binary_tree(num,lst,mid+1,end)
    else:
        return binary_tree(num,lst,start,mid-1)

NM = list(map(int, input(">> ").split()))
N,M = NM[0], NM[1]
lst = list(map(int, input(">> ").split()))
result = 0
H = max(lst)
print(binary_tree(M,lst,0,H))