def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (left+right) // 2

        #check if mid is the target
        if(arr[mid] == target):
            return mid
        
        #if x is greater than target
        elif(arr[mid] < target):
            left = mid+1
        
        else:
            right = mid-1
    
    return -1

arr= [10,20,30,40,50,60]
target = 40

result = binarySearch(arr,target)
value = arr[result]

print(result, value)