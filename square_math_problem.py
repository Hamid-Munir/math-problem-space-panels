def solution(area):
    sol = []
    orginal_values = area

    a = area**(.5)
    b = int(a)
    c = float(b)
    for i in range(area):
        for i in range(area):
            if c == a: 
                value1 = area
                sol.append(value1)
                break
            else:
                area -= 1 
                a = area**(.5)
                b = int(a)
                c = float(b)
                
        area = orginal_values - value1
        if area == 0:
            break 
        orginal_values = area
        a = area**(.5)
        b = int(a)
        c = float(b)
    
    return sol 