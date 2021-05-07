#이진 탐색 연습

def binary_search(array, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, 0, n-1, target)
if result == None:
    print("None")
else:
    print(result+1)