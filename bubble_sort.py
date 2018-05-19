def bubble_sort(anim, drawn_sticks, time = 0):
    n = len(drawn_sticks)
    for i in range(n):
        for j in range(n):
            if drawn_sticks[i][0].number < drawn_sticks[j][0].number:
                temp = drawn_sticks[i][0].number
                anim(i, drawn_sticks[j][0].number)
                anim(j, temp)

