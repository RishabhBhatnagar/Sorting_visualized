from dimensions import anim
def merge(arr, l, m, r, anim):
    n1 = m - l + 1
    n2 = r- m
    L, R = [0 for i in range(n1)], [0 for i in range(n2)]
    for i in range(0 , n1):
        L[i] = arr[l + i][0].number
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j][0].number

    i, j, k = 0, 0, l
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            anim(k, L[i])
            i += 1
        else:
            anim(k, R[j])
            j += 1
        k += 1
    while i < n1:
        anim(k, L[i])
        i += 1
        k += 1
    while j < n2:
        anim(k, R[j])
        j += 1
        k += 1

def mergeSort(drawn_sticks,l,r, anim):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(drawn_sticks, l, m, anim)
        mergeSort(drawn_sticks, m+1, r, anim)
        merge(drawn_sticks, l, m, r, anim)

def merge_sort(anim, drawn_sticks, time = 0.001):
    mergeSort(drawn_sticks, 0, len(drawn_sticks)-1, anim)
