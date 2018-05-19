from dimensions import anim

def next_gap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap

def comb_sort(anim, drawn_sticks, time):
    n = len(drawn_sticks)
    gap = n
    swapped = True
 
    while gap !=1 or swapped == 1:
        gap = next_gap(gap)
        swapped = False
        for i in range(0, n-gap):
            if drawn_sticks[i][0].number > drawn_sticks[i + gap][0].number:
                temp = drawn_sticks[i][0].number
                anim(i, drawn_sticks[i+gap][0].number)
                anim(i+gap, temp)
                '''swap(i, i+gap)
                arr[i], arr[i + gap]=arr[i + gap], arr[i]'''
                swapped = True
