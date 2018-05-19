def gnome_sort(anim, drawn_sticks, time):
    pivot = 0
    while pivot < len(drawn_sticks) - 1:
        if drawn_sticks[pivot][0].number > drawn_sticks[pivot + 1][0].number:
            temp = drawn_sticks[pivot+1][0].number
            anim(pivot + 1, drawn_sticks[pivot][0].number, time)
            anim(pivot, temp, time)
            if pivot > 0:
                pivot -= 2
        pivot += 1
    return drawn_sticks
