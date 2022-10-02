CoinList=[2,2,2,2,2,2,1,2,2,2,2,2,2,2,2]

def Sum(arr, start, end):
    sum = 0
    for i in range(start, end+1):
        sum+= arr[i]
    return sum

def FindFakeCoin(arr, start, end):
    mid = start + (end - start) // 2
    if start > end:
        return -1
    if arr[mid] == 1:
        return mid
    if Sum(arr, start, mid -1 ) < Sum(arr, mid + 1, end):
        return FindFakeCoin(arr, start, mid - 1)
    else:
        return FindFakeCoin(arr, mid + 1, end)
    
print(FindFakeCoin(CoinList, 0, 14))