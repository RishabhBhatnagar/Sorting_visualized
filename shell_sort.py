from dimensions import anim
def shell_sort(anim, drawn_sticks, time):
    n = len(drawn_sticks)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = drawn_sticks[i][0].number
            j = i
            while  j >= gap and drawn_sticks[j-gap][0].number >temp:
                anim(j, drawn_sticks[j-gap][0].number, time)
                #arr[j][0].number = arr[j-gap][0].number
                j -= gap
            anim(j, temp, time)
            #arr[j][0].number = temp
        gap //= 2
