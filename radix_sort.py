'''Source : https://www.geeksforgeeks.org/radix-sort/'''
def countingSort(arr, exp1, time, anim): 
    n = len(arr)
    count =  [0 for i in range(10)]
    output = [0 for i in range(n)]
    for i in range(0, n):
        index = (arr[i][0].number//exp1)
        count[ (index)%10 ] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i][0].number//exp1)
        ###anim(count[(index)%10 ]-1, arr[i][0].number, time)
        output[count[(index)%10 ]-1] = arr[i][0].number
        count[ (index)%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)):
        anim(i, output[i], time)
        #arr[i] = output[i]
        #e=1

def radix_sort(anim, arr, time):
    max1 = max([e[0].number for e in arr])
    exp = 1
    while max1//exp > 0:
        countingSort(arr,exp, time, anim)
        exp *= 10
