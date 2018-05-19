def partition(a, p, r, anim, time):
    x = a[r][0].number
    i = p-1
    for j in range(p, r):
        if a[j][0].number <= x:
            i += 1
            temp = a[i][0].number
            anim(i, a[j][0].number)
            anim(j, temp)
            #a[i], a[j] = a[j], a[i]
    temp = a[i+1][0].number
    anim(r, a[i+1][0].number)
    anim(i+1, temp)
    #a[i+1], a[r] = a[r], a[i+1]
    return i + 1
def quickSort(a, low, high, anim, time):
    if low <= high:
        pivot = partition(a, low, high, anim, time)
        quickSort(a, low, pivot-1, anim, time)
        quickSort(a, pivot+1, high, anim, time)
def quick_sort(anim, drawn_sticks, time):
    quickSort(drawn_sticks, 0, len(drawn_sticks)-1, anim, time)

