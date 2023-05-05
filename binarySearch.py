arr = [1,2,3,3,5,5,5,6,6,7,8,9]
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
 # find x in arr, if x not exist, then find the smallest item that greater than x

