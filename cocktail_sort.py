def swap(i, j, drawn_sticks, anim, time):
    temp = drawn_sticks[i][0].number
    anim(i, drawn_sticks[j][0].number, time)
    anim(j, temp, time)
def cocktail_sort(anim, drawn_sticks, time):
    n = len(drawn_sticks)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range (start, end):
            if drawn_sticks[i][0].number > drawn_sticks[i + 1][0].number :
                swap(i, i+1, drawn_sticks, anim, time)
                swapped = True
        if not swapped : break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if drawn_sticks[i][0].number > drawn_sticks[i + 1][0].number:
                swap(i, i+1, drawn_sticks, anim, time)
                swapped = True
        start = start + 1
