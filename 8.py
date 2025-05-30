def sum_of_intervals(intervals):
    intervals=list(set(intervals))
    intervals.sort()
    i=1
    while i<len(intervals):
        if intervals[i][0]<intervals[i-1][-1]:
            intervals[i-1]=tuple(sorted(intervals[i]+intervals[i-1]))
            intervals.pop(i)
            i-=1
        i+=1
    a=0
    for i in intervals:
        a+=i[-1]-i[0]
    return a
