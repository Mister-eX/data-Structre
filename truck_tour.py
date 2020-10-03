def GasStationTour(gasstations):
    N = len(gasstations)
    start_point = 0
    end_point = 1
    curreent = gasstations[start_point][0] - gasstations[start_point][1]
    
    while curreent < 0 or start_point != end_point:
        while curreent < 0 and start_point != end:
            start_point  = (start_point + 1) % N
            if start_point == 0:
                return -1
        curreent += gasstations[end][0] - gasstations[end][1]
        end = (end + 1) % N
    return start_point