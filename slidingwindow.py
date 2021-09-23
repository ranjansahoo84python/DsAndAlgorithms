def maxSum(arr,windowSize):
    arrSize = len(arr)
    if(arrSize <= windowSize):
        print('Invalid operation')
        return -1
    
    window_sum= sum([arr[i] for i in range(windowSize)])  #first k elements sum
    max_sum = window_sum  ## assign to max_sum for comparison

    for i in range(arrSize-windowSize):
        window_sum= window_sum - arr[i] + arr[i+windowSize] ## remove the left element in window, add a new element in right
        max_sum= max(window_sum,max_sum) ## compare the sum with earlier max

    return max_sum





arr = [80,-50,90,100,150,200,-350,35,120]
k= 2
answer = maxSum(arr,k)
print(answer)


    